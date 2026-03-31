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
# Shape.curve([(32, 32), (25, 24), (17, 34)])
# Shape.curve([(32, 32), (39, 24), (47, 34)])
# Shape.curve([(17, 34), (17, 46), (32, 52)])
# Shape.curve([(47, 34), (47, 46), (32, 52)])


#? BUTTERFLY
# # Body
# Shape.line((32, 20), (32, 50))

# # Left wings
# Shape.curve([(32, 30), (18, 10), (10, 30)])
# Shape.curve([(10, 30), (18, 45), (32, 40)])

# # Right wings (mirror)
# Shape.curve([(32, 30), (46, 10), (54, 30)])
# Shape.curve([(54, 30), (46, 45), (32, 40)])

# # Antennae
# Shape.curve([(32, 20), (28, 10), (26, 15)])
# Shape.curve([(32, 20), (36, 10), (38, 15)])


#? TREE
# # Trunk
# Shape.rect((30, 40), (4, 10))

# # Canopy layers
# Shape.curve([(32, 10), (20, 25), (32, 30)])
# Shape.curve([(32, 10), (44, 25), (32, 30)])

# Shape.curve([(32, 20), (18, 35), (32, 40)])
# Shape.curve([(32, 20), (46, 35), (32, 40)])


#? FISH
# # Body
# Shape.curve([(20, 30), (35, 15), (50, 30)])
# Shape.curve([(20, 30), (35, 45), (50, 30)])

# # Tail
# Shape.polyline([
#     (50, 30), (60, 20), (60, 40), (50, 30)
# ])

# # Eye
# Shape.circle((30, 28), 1)


#? BOW & ARROW
# Bow
# Shape.curve([(20, 20), (10, 35), (20, 50)])

# # String
# Shape.line((20, 20), (20, 50))

# # Arrow shaft
# Shape.line((20, 35), (50, 35))

# # Arrow head
# Shape.polyline([
#     (50, 35), (45, 32), (45, 38), (50, 35)
# ])


#? CASTLE
# # Base
# Shape.rect((20, 35), (24, 15))

# # Towers
# Shape.rect((18, 25), (6, 10))
# Shape.rect((40, 25), (6, 10))

# # Roof curves
# Shape.curve([(21, 25), (21, 20), (24, 25)])
# Shape.curve([(43, 25), (43, 20), (46, 25)])

# # Gate
# Shape.curve([(30, 50), (32, 42), (34, 50)])


#? FLOWER
# # Petals
# Shape.curve([(32, 20), (26, 30), (32, 40)])
# Shape.curve([(32, 20), (38, 30), (32, 40)])

# Shape.curve([(20, 32), (30, 26), (40, 32)])
# Shape.curve([(20, 32), (30, 38), (40, 32)])

# # Center
# Shape.circle((32, 32), 2)

