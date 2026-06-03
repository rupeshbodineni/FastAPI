from fastapi import FastAPI

app=FastAPI()
'''
usage:application root
restapi:http://127.0.0.1:8000/
method:GET
required fields:none
Access type:public
'''
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

'''
usage:create user
restapi:http://127.0.0.1:8000/create
method:POST
required fields:none
Access type:public
'''
@app.post("/create")
def createuser():
    return{"msg":"new user created succesfully"}
'''
usage:fetch user
restiapi:http://127.0.0.1:8000/put
method:put
required fields:none
accesss type:public
'''

@app.get("/put")
def getuser():
   return{"msg":"fetching all users"}

'''
usage:update user
restiapi:http://127.0.0.1:8000/update
method:update
required fields:none
accesss type:public
'''

@app.put("/update")
def updateuser():
    return {"msg": "user updated successfully"}
'''
usage:delete user
restiapi:http://127.0.0.1:8000/delete
method:delete
required fields:none
accesss type:public
'''

@app.delete("/delete")
def deleteuser():
   return{"msg":"user deleted successfully"}