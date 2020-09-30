from alaska_framework.bear import Bear
from .randome_utils import RandomUtils


class BearGenerator:
    BEAR_TYPES = ["POLAR", "BROWN", "BLACK"]
    KEYS = {"bear_id": None, "bear_type": None, "bear_name": None, "bear_age": None}

    @staticmethod
    def generate_bears(amount=10):
        bear_list = []
        for i in range(amount):
            bear = Bear(RandomUtils.get_random_str(), BearGenerator.get_random_type(),
                        RandomUtils.get_random_float())
            bear_list.append(bear)
        return bear_list

    @staticmethod
    def get_random_type():
        return RandomUtils.get_random_from_list(BearGenerator.BEAR_TYPES)
