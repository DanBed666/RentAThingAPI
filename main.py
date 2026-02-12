import pandas
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):
        users_list.append(str(df['id'][i]) + " " + df['name'][i] + " " + df['surname'][i] + " " + str(df['age'][i]))

    return users_list

@app.get("/")
async def root():
    return {"message": "Homepage"}


@app.get("/users")
async def root():
    return JSONResponse(content=get_users(), status_code=200)

