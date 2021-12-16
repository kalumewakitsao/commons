import random
import string


def generate_random_code(size=None):
    size = size or 4
    return ''.join(random.choices(string.ascii_uppercase, k=size))
