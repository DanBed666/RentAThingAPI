import pandas
from models import User

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):

        user = User(int(df['id'][i]), df['name'][i], df['surname'][i], int(df['age'][i]), df['email'][i], df['registerDate'][i])
        users_list.append(user.__dict__)

    return users_list