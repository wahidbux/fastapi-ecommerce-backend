from fastapi import FastAPI

from app.database import engine, Base
import app.models as models
from routers import users, products, cart, orders

# Creates all tables defined in models.py if they don't already exist in
# PostgreSQL. In a production app you'd use Alembic migrations instead,
# but this is fine for a learning project.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="A simple e-commerce backend built with FastAPI, PostgreSQL, and JWT auth.",
    version="1.0.0",
)

# Each router is "plugged in" here — this is what makes /users/*, /products/*,
# /cart/*, and /orders/* all actually reachable.
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "E-Commerce API is running. Visit /docs for interactive API documentation."}