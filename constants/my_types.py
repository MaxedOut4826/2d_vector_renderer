from typing import TypedDict

Vector2 = tuple[int, int]

# class LineParams(TypedDict):
#     start: Vector2
#     end: Vector2
    
class CircleParams(TypedDict):
    centre: Vector2
    radius: int

class RenderParams(TypedDict):
    lines: list[list[Vector2]]
    circles: list[CircleParams]

class Stroke:
    move: int = 0
    line: int = 1
    curve: int = 2

class StrokeParams(TypedDict):
    type: Stroke
    vector: Vector2