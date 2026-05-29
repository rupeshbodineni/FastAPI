from fastapi import FastAPI

app=FastAPI()
'''
usage:application root
restapi:http://127.0.0.1:8000/
method:GET
required fields:none
Access type:public
'''
@app.get("/")
def rootreq():
    return{"msg":"application root request "}

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

#def getuser():
 #   return{"msg":"fetching all users"}
#def updateuser():
 #   return{"msg":"user updated successfully"}
#def deleteuser():
 #   return{"msg":"ser deleted successfully"}