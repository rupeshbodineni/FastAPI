from fastapi import APIRouter

product_Router=APIRouter(prefix="/Product" ,tags= ["products"])
@product_Router.get('/get')
def get():
    return {"message":"product get successfully"}
@product_Router.post('/post')
def create():
    return{"message":"product create successfully"}
@product_Router.put('/put')
def update():
    return{"message":"product updated successfully"}
@product_Router.delete('/delete')
def delete():
    return{"message":"product deleted successfully"}