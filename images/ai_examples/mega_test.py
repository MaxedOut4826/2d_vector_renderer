from .. import Shape

import random

# ======================
# SKY STARS (dense)
# ======================
for x in range(0, 1080, 15):
    for y in range(0, 300, 15):
        if random.random() < 0.2:
            Shape.circle((x, y), 0)


# ======================
# HORIZON
# ======================
Shape.line((0, 300), (1080, 300))


# ======================
# BUILDINGS (LEFT CLUSTER)
# ======================
for i in range(0, 25):
    x = i * 40
    height = random.randint(150, 400)
    width = random.randint(20, 50)

    Shape.rect((x, 300 - height), (width, height))

    # windows
    for wx in range(x + 3, x + width - 3, 6):
        for wy in range(300 - height + 5, 300 - 5, 12):
            if random.random() < 0.35:
                Shape.rect((wx, wy), (2, 4))


# ======================
# CENTRAL TOWERS
# ======================
for i in range(20, 40):
    x = i * 25
    height = random.randint(300, 650)
    width = random.randint(30, 60)

    Shape.rect((x, 300 - height), (width, height))

    # vertical lights
    Shape.line((x + 5, 300 - height), (x + 5, 300))
    Shape.line((x + width - 5, 300 - height), (x + width - 5, 300))

    # window grid
    for wx in range(x + 5, x + width - 5, 8):
        for wy in range(300 - height + 5, 300, 10):
            if random.random() < 0.5:
                Shape.circle((wx, wy), 1)


# ======================
# RIGHT BUILDINGS
# ======================
for i in range(40, 60):
    x = i * 18
    height = random.randint(120, 500)
    width = random.randint(20, 40)

    Shape.rect((x, 300 - height), (width, height))

    # antennas
    Shape.line((x + width // 2, 300 - height), (x + width // 2, 300 - height - 20))

    # windows
    for wx in range(x + 3, x + width - 3, 5):
        for wy in range(300 - height + 5, 300, 10):
            if random.random() < 0.4:
                Shape.rect((wx, wy), (2, 3))


# ======================
# GROUND / ROAD
# ======================
Shape.rect((0, 300), (1080, 420))

# lane markings
for x in range(0, 1080, 40):
    Shape.line((x, 500), (x + 20, 500))


# ======================
# PERSPECTIVE GRID
# ======================
for i in range(0, 50):
    x = i * 20
    Shape.line((540, 300), (x, 720))
    Shape.line((540, 300), (1080 - x, 720))


# ======================
# STREET LIGHTS
# ======================
for x in range(50, 1030, 80):
    Shape.line((x, 300), (x, 650))
    Shape.circle((x, 290), 3)


# ======================
# VEHICLES
# ======================
for i in range(10):
    x = 100 + i * 90
    Shape.rect((x, 600), (40, 20))
    Shape.circle((x + 10, 620), 3)
    Shape.circle((x + 30, 620), 3)


# ======================
# REFLECTION / SHADING LINES
# ======================
for y in range(320, 720, 15):
    Shape.curve([(0, y), (540, y - 20), (1080, y)])