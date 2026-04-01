from .. import Shape
import math

WIDTH = 1600
HEIGHT = 1080

def draw_hd_heart():
    points = []

    resolution = 2000
    scale = 30

    cx = WIDTH // 2
    cy = HEIGHT // 2 + 50

    for i in range(resolution):
        t = (i / resolution) * 2 * math.pi

        x = 16 * math.sin(t)**3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2*t)
            - 2 * math.cos(3*t)
            - math.cos(4*t)
        )

        px = int(cx + x * scale)
        py = int(cy - y * scale)

        points.append((px, py))

    Shape.polygon(points.copy())

    # Optional: clean inner contour (no artifacts)
    for offset in range(15, 100, 20):
        inner = []
        for (px, py) in points:
            dx = px - cx
            dy = py - cy
            length = math.hypot(dx, dy)

            if length <= offset:
                continue

            factor = (length - offset) / length
            inner.append((
                int(cx + dx * factor),
                int(cy + dy * factor)
            ))

        if len(inner) > 2:
            Shape.polyline(inner)


draw_hd_heart()