from fastapi import FastAPI
from Routes.orders import orders_Router
from Routes.products import product_Router 
from Routes.users import users_Router


'''
usage:get index page
restiapi:http://127.0.0.1:8000/
method:get
required fields:none
accesss type:public
'''
app=FastAPI()
@app.get('/')
def index_page():
    return{"message":"this is indexx page"}

app.include_router(orders_Router)
app.include_router(product_Router)
app.include_router(users_Router)