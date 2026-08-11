from fastapi import APIRouter

Product_Router=APIRouter(prefix='/product' , tags=["Products"] )

'''
usage:fetch products
restiapi:http://127.0.0.1:8000/products/get
method:put
required fields:none
accesss type:public
'''


@Product_Router.get("/get")
def get_products():
    return "product fetched succesfully"

'''
usage:post products
restiapi:http://127.0.0.1:8000/products/put
method:put
required fields:none
accesss type:public
'''
@Product_Router.post("/post")
def create_product():
    return " product created successfully"

'''
usage:update products
restiapi:http://127.0.0.1:8000/products/update
method:put
required fields:none
accesss type:public
'''
@Product_Router.put("/put")
def update_product():
    return "product updated successfully"

'''
usage:delete products
restiapi:http://127.0.0.1:8000/products/delete
method:put
required fields:none
accesss type:public
'''
@Product_Router.delete("/delete")
def delete_product():
    return "product deleted successfully"