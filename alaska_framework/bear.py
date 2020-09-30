import json


class Bear:

    def __init__(self, bear_name, bear_type, bear_age, bear_id=None):
        self.name = bear_name
        self.type = bear_type
        self.age = bear_age
        self.id = bear_id
        self.bear_data = json.dumps({"bear_type": self.type, "bear_name": self.name, "bear_age": self.age})

    def change_name(self, new_name):
        self.name = new_name
        self.bear_data = json.dumps({"bear_type": self.type, "bear_name": self.name, "bear_age": self.age})

    def change_id(self, new_id):
        self.id = new_id

    def change_type(self, new_type):
        self.type = new_type
        self.bear_data = json.dumps({"bear_type": self.type, "bear_name": self.name, "bear_age": self.age})

    def change_age(self, new_age):
        self.age = new_age
        self.bear_data = json.dumps({"bear_type": self.type, "bear_name": self.name, "bear_age": self.age})
