from fastapi import FastAPI
#from routes.notes import notes as notes_router
from routes.notes_route import notes
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(notes)
