from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from models import User, Offer
from getdata import get_all, get_with_query, get_by_id

app = FastAPI()
templates = Jinja2Templates('templates')


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.get("/users")
async def get_users():

    content = get_all('data/users.csv', User)

    return JSONResponse(content=content, status_code=200)


@app.get("/users/{user_id}")
async def get_user(user_id: int):

    content = get_by_id('data/users.csv', User, user_id)

    return JSONResponse(content=content, status_code=200)


@app.get("/offers")
async def get_offers(userId: int = None):

    if userId is None:
        content = get_all('data/offers.csv', Offer)
    else:
        content = get_with_query('data/offers.csv', Offer, "userId", userId)

    return JSONResponse(content=content, status_code=200)


@app.get("/offers/{offer_id}")
async def get_offer(offer_id: int):

    content = get_by_id('data/offers.csv', Offer, offer_id)

    return JSONResponse(content=content, status_code=200)
