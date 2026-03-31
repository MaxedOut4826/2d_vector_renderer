from .. import Shape  # adjust import as needed
import random

WIDTH = 1600
HEIGHT = 1080

# ----------------------------
# SKY + GRADIENT BANDING
# ----------------------------
def draw_sky():
    bands = 120
    for i in range(bands):
        y = (HEIGHT * i) / bands
        Shape.rect((0, y), (WIDTH, HEIGHT / bands))

# ----------------------------
# SUN WITH GLOW EFFECT
# ----------------------------
def draw_sun():
    cx, cy = 1300, 180

    # Outer glow rings
    glow_radii = [220, 180, 140, 110, 90]
    for r in glow_radii:
        Shape.circle((cx, cy), r)

    # Core sun
    Shape.circle((cx, cy), 70)

# ----------------------------
# CLOUD SYSTEM (LAYERED)
# ----------------------------
def draw_cloud(x, y, scale=1.0):
    base_offsets = [
        (-80, 0), (-40, -20), (0, -30),
        (40, -20), (80, 0), (0, 20),
        (-20, 20), (20, 20)
    ]

    for dx, dy in base_offsets:
        Shape.circle(
            (x + dx * scale, y + dy * scale),
            int((30 + random.randint(-5, 10)) * scale)
        )

    # Extra fluff layer
    for _ in range(5):
        ox = random.randint(-100, 100) * scale
        oy = random.randint(-40, 40) * scale
        Shape.circle((x + ox, y + oy), int(20 * scale))


def draw_cloud_layer():
    clouds = [
        (200, 150, 1.2),
        (500, 120, 0.9),
        (900, 180, 1.0),
        (1200, 140, 1.3),
        (1400, 220, 0.8)
    ]
    for x, y, s in clouds:
        draw_cloud(x, y, s)

# ----------------------------
# MOUNTAINS (MULTI-LAYER RIDGES)
# ----------------------------
def mountain_ridge(base_y, peaks, jitter=50):
    points = [(0, HEIGHT)]
    points.append((0, base_y))

    step = WIDTH // (len(peaks) - 1)

    for i, peak in enumerate(peaks):
        x = i * step
        y = base_y - peak + random.randint(-jitter, jitter)
        points.append((x, y))

    points.append((WIDTH, base_y))
    points.append((WIDTH, HEIGHT))

    Shape.polygon(points)


def draw_mountains():
    # Far mountains (soft, low peaks)
    mountain_ridge(650, [120, 200, 150, 220, 130, 180, 140], jitter=30)

    # Mid mountains
    mountain_ridge(780, [200, 320, 250, 350, 220, 300, 260], jitter=50)

    # Near mountains (more jagged)
    mountain_ridge(900, [300, 450, 350, 500, 420, 380, 460], jitter=80)

# ----------------------------
# LAKE WITH RIPPLE DETAIL
# ----------------------------
def draw_lake():
    # Main lake body
    Shape.polygon([
        (0, 900),
        (300, 820),
        (600, 880),
        (900, 840),
        (1200, 900),
        (1600, 920),
        (1600, HEIGHT),
        (0, HEIGHT)
    ])

    # Ripple lines
    for i in range(25):
        y = 880 + i * 6
        Shape.line((0, y), (WIDTH, y + random.randint(-3, 3)))

# ----------------------------
# TREES (HYPER-DETAILED)
# ----------------------------
def draw_tree(x, y, scale=1.0):
    # Trunk (multi-segment)
    trunk_height = int(80 * scale)
    trunk_width = int(12 * scale)

    Shape.rect((x, y), (trunk_width, trunk_height))

    # Branch lines
    for i in range(5):
        bx = x + random.randint(-20, 20)
        by = y - random.randint(10, trunk_height)

        Shape.line((x + trunk_width // 2, y), (bx, by))

    # Foliage clusters (layered circles)
    foliage_centers = [
        (x - 20, y - 30),
        (x + 10, y - 60),
        (x + 40, y - 40),
        (x, y - 80)
    ]

    for cx, cy in foliage_centers:
        for _ in range(3):
            Shape.circle(
                (cx + random.randint(-10, 10),
                 cy + random.randint(-10, 10)),
                int(30 * scale)
            )


def draw_forest():
    for i in range(30):
        x = random.randint(0, WIDTH)
        y = random.randint(850, 1000)
        scale = random.uniform(0.6, 1.2)
        draw_tree(x, y, scale)

# ----------------------------
# BIRDS (SMALL V-SHAPES)
# ----------------------------
def draw_birds():
    bird_groups = 20

    for _ in range(bird_groups):
        x = random.randint(200, 1400)
        y = random.randint(100, 400)

        size = random.randint(5, 12)

        # V shape wings
        Shape.line((x, y), (x - size, y + size))
        Shape.line((x, y), (x + size, y + size))

# ----------------------------
# MAIN SCENE
# ----------------------------
def draw_scene():
    draw_sky()
    draw_sun()
    draw_cloud_layer()
    draw_mountains()
    draw_lake()
    draw_forest()
    draw_birds()

# Render the full scene
draw_scene()