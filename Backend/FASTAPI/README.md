FastAPI is a modern Python web framework, very efficient in building APIs. It is based on Pythons type hints feature that has been added since Python 3.6 onwards. It is one of the fastest web frameworks of Python.

As it works on the functionality of **Starlette** and **Pydantic** libraries, its performance is amongst the best and on par with that of NodeJS and Go.

FastAPI doesnt come with any built-in server application. To run FastAPI app, you need an **ASGI** server called **uvicorn**.

The first step in creating a FastAPI app is to declare the application object of FastAPI class.
```
from fastapi import FastAPI
app = FastAPI()
```
This app object is the main point of interaction of the application with the client browser. The uvicorn server uses this object to listen to clients request.

# Documentation
FastAPI generates a schema using **OpenAPI** specifications.

FastAPI uses **Swagger UI** to produce documentation.

<mark>
http://127.0.0.1:8000/docs</mark>

<mark>http://localhost:8000/docs
</mark>

FastAPI also supports another automatic documentation method provided by **Redoc** ( https://github.com/Redocly/redoc).

Enter http://localhost:8000/redoc as URL in the browsers address bar.

**No built-in development server**. Hence we need Uvicorn. It implements **ASGI** standards and is lightning fast. ASGI stands for **Asynchronous Server Gateway Interface.**

**Uvicorn** uses **uvloop** and **httptools** libraries.

```
uvicorn main:app reload
```
The **--reload** option enables the debug mode so that any changes in app.pywill be automatically reflected and the display on the client browser will be automatically refreshed.

Instead of starting Uvicorn server from command line, it can be launched programmatically also.

Example
In the Python code, call uvicorn.run() method, using any of the parameters listed above −
```
import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```
**Uvicorn server will thus be launched in debug mode.**

## FastAPI - Type Hints
FastAPI makes extensive use of the Type hinting feature made available in Pythons version 3.5 onwards.

Pythons new type hinting feature helps in prompting the user with the expected type of the parameters to be passed. This is done by adding a colon and data type after the parameter.
If incompatible values are passed to the function, or returned by the function, Python reports TypeError. Use of **MyPy** static type checker can detect such errors. Install mypy package first.

```
pip3 install mypy
```

## REST Architecture

**RElational State Transfer (REST)** is a software architectural style. REST defines how the architecture of a web application should behave. It is a resource based architecture where everything that the REST server hosts, (a file, an image, or a row in a table of a database), is a resource, having many representations.

REST recommends certain architectural constraints.

```
- Uniform interface

- Statelessness

- Client-server

- Cacheability

- Layered system

- Code on demand
  ```

`REST` <mark>'constraints'</mark> has the following advantages −

```
- Scalability

- Simplicity

- Modifiability

- Reliability

- Portability

- Visibility
```
# Path Parameters with Types
You can use Pythons type hints for the parameters of the function to be decorated. In this case, define name as str and age as int.
```
@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
   return {"name": name, "age":age}
```

## Validations
```
app = FastAPI()
@app.get("/hello/{name}")
async def hello(name:str=Path(...,min_length=3,
max_length=10)):
   return {"name": name}
```

Validation rules can be applied on numeric parameters too, using the operators as given below −
```
gt − greater than

ge − greater than or equal

lt − less than

le − less than or equal
```


## Option 1: Find and Kill the Process Using Port 8000
Run this in the terminal:

``
lsof -i :8000
```
## Option 2: Use a Different Port

**Now kill that process:**
```
kill -9 12345
```


