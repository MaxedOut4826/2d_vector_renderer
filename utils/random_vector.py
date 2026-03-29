from random import randint
from constants.config import SCREEN_SIZE

def random_vector() -> tuple[int, int]:
    return (randint(0, SCREEN_SIZE[0] - 1), randint(0, SCREEN_SIZE[1] - 1))