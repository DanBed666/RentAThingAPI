import os
from dotenv import load_dotenv


load_dotenv('xvariables.env')


def get_var(key_name):

    try:
        return os.environ[key_name]
    except KeyError as e:
        raise KeyError(f"Invalid key: {e}")