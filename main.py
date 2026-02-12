import pandas
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import User

app = FastAPI()

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):
        user = User(int(df['id'][i]), df['name'][i], df['surname'][i], int(df['age'][i]))
        users_list.append(user.__dict__)

    return users_list

@app.get("/")
async def root():
    return {"message": "Homepage"}


@app.get("/users")
async def root():
    return JSONResponse(content=get_users(), status_code=200)

