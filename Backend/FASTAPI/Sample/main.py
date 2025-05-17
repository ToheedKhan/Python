#
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World :-)"}
#

import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}
@app.get("/hello/{name}/{age}")
async def hello(name,age):
   return {"name": name, "age":age}

# If the URL given in the browsers address bar is http://localhost:8000/hello/Ravi/20, The data of Ravi and 20 will be assigned to variables name and age respectively. The browser displays the following JSON response −

# {"name":"Ravi","age":"20"}

# Path Parameters with Types
@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
   return {"name": name, "age":age} 

# The parameter 'name' is a path parameter and 'age' is a query parameter
@app.get("/hello/{name}")
async def hello(name:str,age:int):
   return {"name": name, "age":age}