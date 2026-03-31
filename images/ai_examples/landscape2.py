from .. import Shape

# ======================
# ☀️ SUN + RAYS
# ======================
Shape.circle((120, 12), 8)

# Rays (12 directions)
Shape.line((120, 12), (120, 0))
Shape.line((120, 12), (120, 24))
Shape.line((120, 12), (100, 12))
Shape.line((120, 12), (140, 12))

Shape.line((120, 12), (105, 0))
Shape.line((120, 12), (135, 0))
Shape.line((120, 12), (105, 24))
Shape.line((120, 12), (135, 24))

Shape.line((120, 12), (110, 5))
Shape.line((120, 12), (130, 5))
Shape.line((120, 12), (110, 19))
Shape.line((120, 12), (130, 19))


# ======================
# ⛰️ FAR MOUNTAINS
# ======================
Shape.polyline([(0, 50), (20, 20), (40, 50)])
Shape.polyline([(30, 50), (55, 18), (80, 50)])
Shape.polyline([(70, 50), (95, 22), (120, 50)])
Shape.polyline([(110, 50), (135, 25), (156, 50)])

# secondary layer
Shape.polyline([(10, 55), (30, 30), (50, 55)])
Shape.polyline([(45, 55), (70, 28), (95, 55)])
Shape.polyline([(90, 55), (115, 32), (140, 55)])


# ======================
# 🌆 CITY SKYLINE
# ======================
Shape.rect((10, 40), (6, 20))
Shape.rect((18, 35), (8, 25))
Shape.rect((28, 45), (5, 15))
Shape.rect((35, 38), (10, 22))
Shape.rect((48, 42), (6, 18))
Shape.rect((56, 36), (8, 24))
Shape.rect((66, 44), (5, 16))
Shape.rect((74, 39), (9, 21))

# antennae
Shape.line((22, 35), (22, 28))
Shape.line((40, 38), (40, 30))
Shape.line((60, 36), (60, 29))


# ======================
# 🌉 BRIDGE (detailed)
# ======================
Shape.line((20, 60), (130, 60))

# arches
Shape.curve([(20, 60), (30, 50), (40, 60)])
Shape.curve([(40, 60), (50, 50), (60, 60)])
Shape.curve([(60, 60), (70, 50), (80, 60)])
Shape.curve([(80, 60), (90, 50), (100, 60)])
Shape.curve([(100, 60), (110, 50), (120, 60)])
Shape.curve([(120, 60), (125, 50), (130, 60)])

# supports
Shape.line((30, 60), (30, 70))
Shape.line((50, 60), (50, 70))
Shape.line((70, 60), (70, 70))
Shape.line((90, 60), (90, 70))
Shape.line((110, 60), (110, 70))


# ======================
# 🌊 RIVER (multi-layer)
# ======================
Shape.curve([(0, 70), (40, 55), (80, 70)])
Shape.curve([(80, 70), (120, 85), (156, 70)])

Shape.curve([(0, 72), (40, 57), (80, 72)])
Shape.curve([(80, 72), (120, 87), (156, 72)])

Shape.curve([(0, 74), (40, 59), (80, 74)])
Shape.curve([(80, 74), (120, 89), (156, 74)])


# ======================
# 🌳 TREES (cluster left)
# ======================
for x in [5, 12, 18]:
    Shape.rect((x, 60), (2, 8))
    Shape.curve([(x+1, 50), (x-4, 60), (x+1, 65)])
    Shape.curve([(x+1, 50), (x+6, 60), (x+1, 65)])


# ======================
# 🌳 TREES (cluster right)
# ======================
for x in [135, 142, 148]:
    Shape.rect((x, 60), (2, 8))
    Shape.curve([(x+1, 50), (x-4, 60), (x+1, 65)])
    Shape.curve([(x+1, 50), (x+6, 60), (x+1, 65)])


# ======================
# ☁️ CLOUDS (many layers)
# ======================
Shape.curve([(20, 10), (30, 5), (40, 10)])
Shape.curve([(40, 10), (50, 5), (60, 10)])
Shape.curve([(30, 10), (40, 15), (50, 10)])

Shape.curve([(70, 8), (80, 3), (90, 8)])
Shape.curve([(90, 8), (100, 3), (110, 8)])
Shape.curve([(80, 8), (90, 13), (100, 8)])

Shape.curve([(100, 20), (110, 15), (120, 20)])
Shape.curve([(120, 20), (130, 15), (140, 20)])
Shape.curve([(110, 20), (120, 25), (130, 20)])


# ======================
# 🛣️ ROAD (foreground)
# ======================
Shape.line((0, 77), (156, 77))

Shape.line((40, 77), (70, 65))
Shape.line((116, 77), (86, 65))

# dashed center
for x in range(10, 150, 15):
    Shape.line((x, 76), (x+5, 76))


# ======================
# 🌉 EXTRA DETAIL (rails)
# ======================
Shape.line((20, 58), (130, 58))
Shape.line((20, 62), (130, 62))