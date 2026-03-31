from math import floor
from sys import stdout
from . import SCREEN_SIZE, CELL_VALUES, circle_symmetry, clear_screen, replace_chars
from renderer.shapes import Shape

class Renderer:
    screen_data: list[str] = [CELL_VALUES[0] * SCREEN_SIZE[0]] * (floor(SCREEN_SIZE[1] / 2))
    screen: str = ""
        
    @staticmethod
    def draw_pixel(x: int, y: int) -> None:
        if (0 > x or x > SCREEN_SIZE[0] - 1 or 0 > y or y > SCREEN_SIZE[1] - 1): return
            
        data = 1 if y % 2 == 0 else 2
        y = y // 2
        pixel = Renderer.screen_data[y][x]
        
        bit: str = CELL_VALUES[data | CELL_VALUES.index(pixel)]
        
        Renderer.screen_data[y] = replace_chars(Renderer.screen_data[y], bit, x, 1)
                    
    # Bresenham's Line Algorithm
    @staticmethod
    def draw_line(x0: int, y0: int, x1: int, y1: int) -> None:
        dx: int = abs(x1 - x0)
        dy: int = abs(y1 - y0)

        sx: int = 1 if x0 < x1 else -1
        sy: int = 1 if y0 < y1 else -1

        err: int = dx - dy

        while True:
            Renderer.draw_pixel(x0, y0)

            if x0 == x1 and y0 == y1: break
            
            e2 = 2 * err

            if e2 > -dy:
                err -= dy
                x0 += sx

            if e2 < dx:
                err += dx
                y0 += sy
                
    # Middlepoint Circle Algorithm
    @staticmethod
    def draw_circle(cx: int, cy: int, r: int) -> None:
        t1: float = r / 16
        x: int = r
        y: int = 0
        
        while x >= y:
            for px, py in circle_symmetry(cx, cy, x, y):
                Renderer.draw_pixel(px, py)

            y = y + 1
            t1 = t1 + y
            t2 = t1 - x
            
            if t2 >= 0:
                t1 = t2
                x = x - 1
    
    @staticmethod
    def draw_screen():
        clear_screen()        
        for line in Shape.render_queue["lines"]:
            x0, y0 = line["start"]
            x1, y1 = line["end"]
            Renderer.draw_line(x0, y0, x1, y1)
            
        for circle in Shape.render_queue["circles"]:
            cx, cy = circle["centre"]
            Renderer.draw_circle(cx, cy, circle["radius"])
                    
        for xy in Renderer.screen_data:
            Renderer.screen += "".join(xy) + "\n"
                    
        stdout.write(Renderer.screen)
        stdout.flush()