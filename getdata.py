import dataclasses
import pandas


def get_all(file_name, class_name):

    users_list = []
    df = pandas.read_csv(file_name)

    for i in range(df.shape[0]):

        element = to_obj(df.iloc[i], class_name)
        users_list.append(element.__dict__)

    return users_list


def get_with_query(file_name, class_name, field_name, value):

    users_list = []
    df = pandas.read_csv(file_name)

    for i in range(df.shape[0]):

        if df.iloc[i][f'{field_name}'] == value:
            element = to_obj(df.iloc[i], class_name)
            users_list.append(element.__dict__)

    return users_list


def get_by_id(file_name, class_name, element_id):

    df = pandas.read_csv(file_name)
    element = {"detail": "Not found"}

    for i in range(df.shape[0]):

        if df.iloc[i]['id'] == element_id:
            element = to_obj(df.iloc[i], class_name).__dict__
            break

    return element

def to_obj(data, class_name):

    element_dict = {}

    types = [int, bool, float]

    for field in dataclasses.fields(class_name):

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

    return class_name(**element_dict)