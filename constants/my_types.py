from typing import TypedDict

Vector2 = tuple[int, int]

class LineParams(TypedDict):
    start: Vector2
    end: Vector2
    
class CircleParams(TypedDict):
    centre: Vector2
    radius: int

class RenderParams(TypedDict):
    lines: list[LineParams]
    circles: list[CircleParams]