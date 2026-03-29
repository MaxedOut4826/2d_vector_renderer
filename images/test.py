from . import Shape
from utils.random_vector import random_vector
from random import randint

# for i in range(randint(1, 5)):
#     rand = random_vector()
#     Shape.circle(rand, randint(1, 32))

for i in range(randint(1, 10)):
    Shape.polygon([random_vector(), random_vector(), random_vector()])
