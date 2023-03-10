from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )

#user crud operations
class User(BaseModel):
    name : str
    email : str
    password : str
    created_at : str = datetime.now()

@app.post('/user')
async def create_user(user : User):
    try :
        client.jober.user.insert_one(dict(user))
        return True
    except Exception as e :
        print(str(e))
        return False

@app.get("/user")
async def get_user(email : str):
    try:
        filter = {
            'email' : email
        }
        project = {
            '_id' : 0,
        }
        client.jober.user.find(filter=filter, project=project)
        return True
    except Exception as e:
        print(str(e))
        return False

class CUser(BaseModel):
    query : dict = {}
    key : str
    value : str

@app.put('/user')
async def change_user(user : CUser):
    try: 
        filter = user.query
        update = {
            '$set' : {
                user.key : user.value
            }
        }
        client.jober.user.update(filter=filter, update = update)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.delete('/user')
async def delete_user(email:str):
    try:
        filter = {
            'email' :email
        }
        client.jober.user.delete_one(filter=filter)
        return True
    except Exception as e:
        print(str(e))
        return False
# user crud operations ends here