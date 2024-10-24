
from fastapi import FastAPI
from starlette.requests import Request

from services import save_user_objects, get_user_objects
from settings import *
app = FastAPI()




@app.post('/save')
async def save_data(request: Request):
    body = await request.json()
    await save_user_objects(body["username"], body["objects"])



@app.post('/get')
async def get_data(request: Request):
    body = await request.json()
    objects =await get_user_objects(body["username"])
    return objects
