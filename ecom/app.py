from fastapi import FastAPI
from Routes.orders import orders_Router
from Routes.products import product_Router
from Routes.users import users_Router

from database.database import engine, Base
from database.models import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def index_page():
    return {"message": "this is index page"}

app.include_router(orders_Router)
app.include_router(product_Router)
app.include_router(users_Router)