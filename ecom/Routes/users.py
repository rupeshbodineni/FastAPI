from fastapi import APIRouter

users_Router=APIRouter(prefix="/users" ,tags=["users"])
@users_Router.get('/get')
def get():
    return {"message":"users get successfully"}
@users_Router.post('/post')
def create():
    return{"message":"user created successfully"}
@users_Router.put('/put')
def update():
    return {"message":"user updated successfully"}
@users_Router.delete('/delete')
def delete():
    return {"message":"user deleted successfully"}