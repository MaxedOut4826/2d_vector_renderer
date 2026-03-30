from . import Shape
from utils.random_vector import random_vector
from random import randint

# for i in range(randint(1, 5)):
#     rand = random_vector()
#     Shape.circle(rand, randint(1, 32))

# for i in range(randint(1, 10)):
#     Shape.polygon([random_vector(), random_vector(), random_vector()])

Shape.polygon([(32, 32), (30, 28), (27, 27), (22, 27), (19, 29),
               (17, 32), (17, 37),
               (23, 45), (32, 52), (41, 45),
               (47, 37), (47, 32),
               (44, 28), (42, 27), (37, 27), (34, 28), (33, 29)]) #? HEART