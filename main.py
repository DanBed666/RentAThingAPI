import pandas
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import User
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates('templates')

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):
        user = User(int(df['id'][i]), df['name'][i], df['surname'][i], int(df['age'][i]))
        users_list.append(user.__dict__)

    return users_list

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.get("/users")
async def root():
    return JSONResponse(content=get_users(), status_code=200)

