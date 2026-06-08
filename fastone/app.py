from fastapi import FastAPI
from Routes.products import Product_Router
from Routes.users import Users_Router

app = FastAPI()
'''
usage:get routers
restiapi:http://127.0.0.1:8000/get
method:get
required fields:none
accesss type:public

'''
@app.get("/get")
def index_page():
    return {"msg": "fetching all users"}

app.include_router(Product_Router)
app.include_router(Users_Router)

