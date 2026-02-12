import pandas
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello WOrld"}


if __name__ == '__main__':

    excel_data = pandas.read_csv('data/users.csv')

    for e in excel_data.values:
        print(e)