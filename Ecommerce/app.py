from fastapi import FastAPI
from Routes.products import products


app=FastAPI()
@app.get('\get')
def get():
    return {"message":"this is index page"}

app.include_router(products)