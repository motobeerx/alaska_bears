from utils.dictionary_utils import json_to_python
from configurations.alaska_config import AlaskaConfig
import requests


class Request:
    def create_bear(self, bear):
        response = requests.post(AlaskaConfig.ALASKA_BEAR, bear.bear_data)
        bear.change_id(response.text)
        return bear.id

    def delete_bear(self, bear):
        response = requests.delete(AlaskaConfig.ALASKA_SPECIFIC_BEAR.format(id=bear.id))
        return response.text

    def delete_all_bears(self):
        response = requests.delete(AlaskaConfig.ALASKA_BEAR)
        return response.text

    def update_bear(self, bear):
        response = requests.put(AlaskaConfig.ALASKA_SPECIFIC_BEAR.format(id=bear.id), bear.bear_data)
        return response.text

    def view_all_bears(self):
        response = requests.get(AlaskaConfig.ALASKA_BEAR)
        response = json_to_python(response.text)
        return response

    def view_bear(self, bear):
        response = requests.get(AlaskaConfig.ALASKA_SPECIFIC_BEAR.format(id=bear.id))
        response = json_to_python(response.text)
        return response

    def is_bear(self, bear):
        return True if self.is_bear_name(bear) and self.is_bear_type(bear) and self.is_bear_age(bear) else False

    def is_bear_name(self, bear):
        bear_in_alaska = self.view_bear(bear)
        return False if bear_in_alaska is None or bear_in_alaska['bear_name'] != str(bear.name) else True

    def is_bear_type(self, bear):
        bear_in_alaska = self.view_bear(bear)
        return False if bear_in_alaska is None or bear_in_alaska['bear_type'] != bear.type else True

    def is_bear_age(self, bear):
        bear_in_alaska = self.view_bear(bear)
        return False if bear_in_alaska is None or bear_in_alaska['bear_age'] != bear.age else True
