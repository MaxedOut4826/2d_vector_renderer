from constants.my_types import Vector2
from os import get_terminal_size

CELL_VALUES: tuple[str, ...] = (" ", "▀", "▄", "█")
# SCREEN_SIZE: Vector2 = (156, 78)
# SCREEN_SIZE: Vector2 = (1600, 1080)

SCREEN_SIZE: Vector2 = (get_terminal_size()[0], get_terminal_size()[1] * 2)
