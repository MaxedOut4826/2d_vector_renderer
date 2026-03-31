from . import Shape
# from utils.random_vector import random_vector
# from random import randint

#? RANDOM CIRCLES
# for i in range(randint(1, 5)):
#     rand = random_vector()
#     Shape.circle(rand, randint(1, 32))


#? RANDOM POLYGONS
# for i in range(randint(1, 10)):
#     Shape.polygon([random_vector(), random_vector(), random_vector()])


#? HEART WITH LINES
# Shape.polygon([(32, 32), (30, 28), (27, 27), (22, 27), (19, 29),
#                (17, 32), (17, 37),
#                (23, 45), (32, 52), (41, 45),
#                (47, 37), (47, 32),
#                (44, 28), (42, 27), (37, 27), (34, 28), (33, 29)])


#? RANDOM CURVES
# points: list[tuple[int, int]] = []

# for i in range(randint(3, 10)):
#     points.append(random_vector())
    
# Shape.curve(points)


#? HEART WITH CURVES
Shape.curve([(32, 32), (25, 24), (17, 34)])
Shape.curve([(32, 32), (39, 24), (47, 34)])
Shape.curve([(17, 34), (17, 46), (32, 52)])
Shape.curve([(47, 34), (47, 46), (32, 52)])