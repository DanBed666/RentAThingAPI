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

    types = [int, bool, float]

    for field in dataclasses.fields(classname):

        for t in types:

            if not pandas.isna(data[field.name]):
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