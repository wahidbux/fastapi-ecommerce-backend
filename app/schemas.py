from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# ---------- User schemas ----------

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True  # allows Pydantic to read data from SQLAlchemy objects


class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- Product schemas ----------

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0


class ProductOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        from_attributes = True


# ---------- Cart schemas ----------

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1


class CartItemOut(BaseModel):
    id: int
    quantity: int
    product: ProductOut

    class Config:
        from_attributes = True


# ---------- Order schemas ----------

class OrderItemOut(BaseModel):
    id: int
    quantity: int
    price_at_purchase: float
    product: ProductOut

    class Config:
        from_attributes = True


class OrderOut(BaseModel):
    id: int
    total_price: float
    status: str
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True