from fastapi import  APIRouter

orders_Router=APIRouter(prefix="/orders" ,tags=["orders"])

@orders_Router.get('/get')
def get():
    return {"Message":"orders get successfully"}
@orders_Router.post('/post')
def create():
    return {"message":"order created successfully"}
@orders_Router.put('/put')
def update():
    return {"message":"orders updates successfully"}
@orders_Router.delete('/delete')
def delete():
    return {"messsage":"order deleted succefully"}