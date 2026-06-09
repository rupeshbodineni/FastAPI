from fastapi import APIRouter
from pydantic import BaseModel

product_Router=APIRouter(prefix="/Product" ,tags= ["products"])
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int
products=[
  {
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop for work and gaming",
    "price": 75000,
    "quantity": 10
  },
  {
    "id": 2,
    "name": "Smartphone",
    "description": "Latest Android smartphone with AMOLED display",
    "price": 25000,
    "quantity": 25
  },
  {
    "id": 3,
    "name": "Headphones",
    "description": "Wireless noise-cancelling headphones",
    "price": 5000,
    "quantity": 50
  },
  {
    "id": 4,
    "name": "Keyboard",
    "description": "Mechanical keyboard with RGB lighting",
    "price": 3000,
    "quantity": 40
  },
  {
    "id": 5,
    "name": "Mouse",
    "description": "Wireless ergonomic mouse",
    "price": 1500,
    "quantity": 60
  }
]
@product_Router.get('/get')
def get():
    return products

@product_Router.get('/{id}')
def get_user_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return {"message": "Product not found"}


@product_Router.post('/post')
def add_product(product: Product):
    products.append(product.dict())
    return {"message": "product added successfully"} 
    return {"message":"product not found"}


@product_Router.put('/put')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i]["id"] == id:
            products[i] = product.model_dump()
            return {"message": "product updated successfully"}

    return {"message": "product not found"}

@product_Router.delete('/delete')
def delete_product():
    for i in range(len(products)):
     if products[i].id == id:
        return {"message": "product deleted successfully"}
    return {"message": "product not found"}