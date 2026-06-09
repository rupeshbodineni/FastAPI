from fastapi import APIRouter

products=APIRouter(prefix="/products")
@products.get('/get')
def get():
    return products
@products.get('/get/{id}')
def get_product_byid(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "product not found"}
@products.post('/post')
def create():
    return {"message":"product created successfully"}
@products.put('/put')
def update():
    return{"message":"product updated successfully"}
@products.delete('/delete')
def delete():
    return {"message":"product delete successfully"}