from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://toheedkhan:hogizreviY3EDmkv@tutorial.vndlwfk.mongodb.net")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = conn.notes.notes.find_one({})
    # print(docs)
    docs = conn.notes.notes.find({})
    for doc in docs:
        print(doc)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )

#("item.html", {"request": request, "id": id})