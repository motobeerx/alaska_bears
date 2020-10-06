import json


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def json_string_to_dictionary_object(plain_text):
    response = json.loads(plain_text)
    response = Struct(**response)
    return response


def json_to_python(plain_text):
    try:
        dictionary = json.loads(plain_text)
        return dictionary
    except json.JSONDecodeError:
        return None
