import dataclasses
import pandas

from models import User


def get_elements(filename, classname):

    users_list = []
    df = pandas.read_csv(filename)

    for i in range(df.shape[0]):

        element = to_obj(df.iloc[i], classname)
        users_list.append(element.__dict__)

    return users_list

def to_obj(data, classname):

    element_dict = {}

    types = [int, bool, float]

    for field in dataclasses.fields(classname):

        if not pandas.isna(data[field.name]):
            for t in types:
                try:
                    if field.type is t:
                        element_dict[field.name] = t(data[field.name])
                        break
                    else:
                        element_dict[field.name] = data[field.name]
                except ValueError:
                    element_dict[field.name] = field.default
        else:
            element_dict[field.name] = field.default

    return classname(**element_dict)

if __name__ == "__main__":

    df = pandas.read_csv("data/offers.csv")

    e = df.iloc[0:4]

    #element = to_obj(e, User)
    #print(element.__dict__)

    ile = 0

    for i in range(df.shape[0]):

        if df.iloc[i]['userId'] == 1:
            print(df.iloc[i])
            ile = ile + 1

    print(ile)

        #element = to_obj(df.iloc[i], User)
        #print(df.iloc[i])
        #print(element.__dict__)

