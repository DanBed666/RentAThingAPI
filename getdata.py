import pandas
from models import User, Offer

def get_users():

    users_list = []
    df = pandas.read_csv('data/users.csv')

    for i in range(df.shape[0]):

        user = User(int(df['id'][i]), df['name'][i], df['surname'][i], int(df['age'][i]), df['email'][i], df['registerDate'][i])
        users_list.append(user.__dict__)

    return users_list

def get_offers():

    offers_list = []
    df = pandas.read_csv('data/offers.csv')

    for i in range(df.shape[0]):

        offer = Offer(int(df['userId'][i]), int(df['offerId'][i]), df['title'][i], df['description'][i], df['price'][i], df['offerCreateDate'][i], bool(df['isOfferEnd'][i]))
        offers_list.append(offer.__dict__)

    return offers_list