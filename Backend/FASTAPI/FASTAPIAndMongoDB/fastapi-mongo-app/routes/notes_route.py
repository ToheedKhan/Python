from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

from models.note import Note

from schemas.note import notesEntity, noteEntity
from config.db import conn



notes = APIRouter()

templates = Jinja2Templates(directory="templates")


@notes.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = conn.notes.notes.find_one({})
    print("Hi")
    docs = conn.notes.notes.find({})
    print(docs)
    newDocs = []
    for doc in docs:
        print(doc)
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse(
            "index.html", {"request": request, "newDocs": newDocs}
        )

@notes.post("/")
async def add_note(request: Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    print(formDict)
    note = conn.notes.notes.insert_one(formDict)
    return {"success" : True}
    # return templates.TemplateResponse(
    #         "index.html", {"request": request, "newDocs": newDocs}
    #     ) 


# @notes.post("/")
# async def add_note(note: Note):
#     # new_note = {
#     #     "title": note.title,
#     #     "desc": note.desc,
#     #     "important": note.important
#     # }
#     # conn.notes.notes.insert_one(new_note)
#     # return {"message": "Note added successfully", "note": new_note}

#     inserted_note = conn.notes.notes.insert_one(dict)
#     return noteEntity(inserted_note)



# @notes.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}
