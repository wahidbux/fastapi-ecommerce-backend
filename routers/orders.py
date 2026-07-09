from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
import app.models as models
import app.schemas as schemas
import app.auth as auth

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/checkout", response_model=schemas.OrderOut)
def checkout(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    cart_items = db.query(models.CartItem).filter(models.CartItem.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Re-check stock for every item before finalizing the order — stock could
    # have changed since items were added to the cart.
    for cart_item in cart_items:
        if cart_item.product.stock < cart_item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for '{cart_item.product.name}'",
            )

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    new_order = models.Order(
        user_id=current_user.id,
        total_price=total_price,
        status="paid",  # simulated payment — always succeeds in this simplified version
    )
    db.add(new_order)
    db.flush()  # assigns new_order.id without fully committing yet, so we can use it below

    for cart_item in cart_items:
        order_item = models.OrderItem(
            order_id=new_order.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price_at_purchase=cart_item.product.price,
        )
        cart_item.product.stock -= cart_item.quantity  # reduce stock
        db.add(order_item)
        db.delete(cart_item)  # clear the cart

    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=List[schemas.OrderOut])
def list_orders(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return db.query(models.Order).filter(models.Order.user_id == current_user.id).all()


@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    order = (
        db.query(models.Order)
        .filter(models.Order.id == order_id, models.Order.user_id == current_user.id)
        .first()
    )
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order