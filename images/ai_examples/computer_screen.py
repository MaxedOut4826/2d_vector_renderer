from .. import Shape


# ======================
# 🧱 MAIN WINDOW FRAME
# ======================
Shape.rect((5, 5), (146, 70))


# ======================
# 🧾 TITLE BAR
# ======================
Shape.rect((5, 5), (146, 8))

# window controls (left)
Shape.circle((10, 9), 1)
Shape.circle((15, 9), 1)
Shape.circle((20, 9), 1)


# ======================
# 📊 LEFT PANEL (stats)
# ======================
Shape.rect((8, 15), (40, 55))

# divider lines
Shape.line((8, 25), (48, 25))
Shape.line((8, 35), (48, 35))
Shape.line((8, 45), (48, 45))
Shape.line((8, 55), (48, 55))

# mini bars
Shape.line((12, 60), (12, 50))
Shape.line((16, 60), (16, 45))
Shape.line((20, 60), (20, 52))
Shape.line((24, 60), (24, 48))


# ======================
# 📈 MAIN GRAPH PANEL
# ======================
Shape.rect((52, 15), (90, 35))

# grid lines
for y in range(20, 50, 5):
    Shape.line((52, y), (142, y))

for x in range(60, 140, 10):
    Shape.line((x, 15), (x, 50))

# graph curve
Shape.curve([(55, 45), (80, 30), (110, 35), (135, 25)])


# ======================
# 📦 BOTTOM MODULES
# ======================
Shape.rect((52, 52), (40, 18))
Shape.rect((92, 52), (50, 18))

# inner separators
Shape.line((52, 60), (92, 60))
Shape.line((92, 60), (142, 60))


# ======================
# 🔘 BUTTON CLUSTER
# ======================
for i, x in enumerate([60, 70, 80, 90]):
    Shape.circle((x, 66), 2)


# ======================
# 🧾 TEXT-LIKE LINES (UI placeholders)
# ======================
Shape.line((10, 18), (30, 18))
Shape.line((10, 22), (35, 22))
Shape.line((10, 28), (32, 28))

Shape.line((10, 38), (38, 38))
Shape.line((10, 42), (28, 42))
Shape.line((10, 48), (36, 48))


# ======================
# 📡 STATUS INDICATORS
# ======================
Shape.circle((135, 10), 1)
Shape.circle((140, 10), 1)
Shape.circle((145, 10), 1)

# connection line
Shape.line((130, 10), (145, 10))


# ======================
# 🧩 DIAGNOSTIC MINI CHART
# ======================
Shape.rect((100, 52), (40, 18))

Shape.curve([(105, 65), (115, 58), (125, 62)])
Shape.curve([(125, 62), (132, 60), (138, 66)])