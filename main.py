import pandas
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import User
from fastapi.templating import Jinja2Templates
from datetime import datetime
from zoneinfo import ZoneInfo


app = FastAPI()
templates = Jinja2Templates('templates')

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):
        dt_utc = datetime.fromisoformat(df['registerDate'][i].replace("Z", "+00:00"))
        dt_local = dt_utc.astimezone(ZoneInfo("Europe/Warsaw"))
        json_date = dt_local.strftime("%d-%m-%Y %H:%M:%S")

        user = User(int(df['id'][i]), df['name'][i], df['surname'][i], int(df['age'][i]), df['email'][i], json_date)
        users_list.append(user.__dict__)

    return users_list

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.get("/users")
async def root():
    return JSONResponse(content=get_users(), status_code=200)

