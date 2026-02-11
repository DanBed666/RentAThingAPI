import pandas


def print_hi(name):

    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


    excel_data = pandas.read_csv('data/users.csv')

    for e in excel_data.values:
        print(e)