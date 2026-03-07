from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from models import User, Offer
import getdata

app = FastAPI()
templates = Jinja2Templates('templates')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get("/users")
async def get_users():
    return JSONResponse(content=getdata.get_elements('data/users.csv', User), status_code=200)

@app.get("/offers")
async def get_offers():
    return JSONResponse(content=getdata.get_elements('data/offers.csv', Offer), status_code=200)

