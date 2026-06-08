from fastapi import APIRouter

Users_Router = APIRouter(prefix="/user", tags=["Users"])
'''
usage:application root
restapi:http://127.0.0.1:8000/get
method:GET
required fields:none
Access type:public
'''
@Users_Router.get("/users")
def get_user():
    return " user get successfully"
'''
usage:create user
restapi:http://127.0.0.1:8000/create
method:POST
required fields:none
Access type:public
'''
@Users_Router.post("/create")
def createuser():
    return{"msg":"new user created succesfully"}
'''
usage:fetch user
restiapi:http://127.0.0.1:8000/put
method:put
required fields:none
accesss type:public
'''

@Users_Router.get("/get")
def getuser():
   return{"msg":"fetching all users"}

'''
usage:update user
restiapi:http://127.0.0.1:8000/update
method:update
required fields:none
accesss type:public
'''

@Users_Router.put("/update")
def updateuser():
    return {"msg": "user updated successfully"}
'''
usage:delete user
restiapi:http://127.0.0.1:8000/delete
method:delete
required fields:none
accesss type:public
'''

@Users_Router.delete("/delete")
def deleteuser():
   return{"msg":"user deleted successfully"}