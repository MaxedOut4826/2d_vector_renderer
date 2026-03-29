from constants.my_types import Vector2

def circle_symmetry(cx: int, cy: int, x: int, y: int) -> list[Vector2]:
    return [
        (cx + x, cy + y),
        (cx - x, cy + y),
        (cx + x, cy - y),
        (cx - x, cy - y),
        (cx + y, cy + x),
        (cx - y, cy + x),
        (cx + y, cy - x),
        (cx - y, cy - x),
    ]