from string import ascii_uppercase
import random


class RandomUtils:
    LENGTH = 10
    LOWER_BOUND = 1
    UPPER_BOUND = 52

    @staticmethod
    def get_random_str(length=LENGTH):
        return ''.join(random.choice(ascii_uppercase) for i in range(length))

    @staticmethod
    def get_random_int(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
        return random.randint(lower_bound, upper_bound)

    @staticmethod
    def get_random_float(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
        return random.uniform(lower_bound, upper_bound)

    @staticmethod
    def get_random_from_list(items):
        i = RandomUtils.get_random_int(0, len(items)-1)
        return items[i]
