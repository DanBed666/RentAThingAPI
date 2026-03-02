import dataclasses
import pandas

def get_elements(filename, classname):

    users_list = []
    df = pandas.read_csv(filename)

    print(df.shape)

    for i in range(df.shape[0]):

        element = to_obj(df.iloc[i], classname)
        users_list.append(element.__dict__)

    return users_list

def to_obj(data, classname):

    element_dict = {}

    for field in dataclasses.fields(classname):

        element_dict[field.name] = data[field.name]

    return classname(**element_dict)