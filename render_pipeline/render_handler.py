from math import floor
from sys import stdout
from os import system as terminal, name as operation_system
from render_pipeline.shapes import Shape
from . import SCREEN_SIZE, CELL_VALUES, circle_symmetry, replace_chars

class Renderer:
    frame_buffer: list[str] = [CELL_VALUES[0] * SCREEN_SIZE[0]] * (floor(SCREEN_SIZE[1] / 2))
    frame: str = ""
       
    @staticmethod
    def draw_pixel(x: int, y: int) -> None:
        if (0 > x or x > SCREEN_SIZE[0] - 1 or 0 > y or y > SCREEN_SIZE[1] - 1): return
            
        data = 1 if y % 2 == 0 else 2
        x = int(x)
        y = int(y // 2)
        pixel = Renderer.frame_buffer[y][x]
        
        bit: str = CELL_VALUES[data | CELL_VALUES.index(pixel)]
        
        Renderer.frame_buffer[y] = replace_chars(Renderer.frame_buffer[y], bit, x, 1)
                    
                    
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
    def draw_frame():
        Renderer.clear_frame()
        for line in Shape.render_queue["lines"]:
            x0, y0 = line[0]
            x1, y1 = line[1]
            
            Renderer.draw_line(x0, y0, x1, y1)
            
        for circle in Shape.render_queue["circles"]:
            cx, cy = circle["centre"]
            
            Renderer.draw_circle(cx, cy, circle["radius"])
                    
        for xy in Renderer.frame_buffer:
            Renderer.frame += "".join(xy) + "\n"
                    
        stdout.write(Renderer.frame)
        stdout.flush()
        
        
    @staticmethod
    def clear_frame():
        if operation_system == "nt":
            terminal("cls")
        else:
            terminal("clear")
            
            

#? FOR EACH PIXEL IN THE LINE DRAW ONLY CALL THE DRAW PIXEL IF THE PIXEL IS NOT ALREADY FULL
#! FOR EACH PIXEL IN THE PIXEL DRAW SKIP IF THE PIXEL DATA IS THE SAME AS THE CELL VALUE

#! ADD DYNAMIC FRAME RESIZING

#! IMPORTANT ANSI COMMANDS FOR REPEATED FRAME GENERATION OPTIMISATION:
#* "\033[H"  <--- Move Cursor to Top Left (GOOD TO OVERRIDE PREVIOUS TEXT)
#* "\033[2J"  <--- Clear Screen (MUST USE)
#* "\033[?25l"  <--- Hide Cursor (USEFUL)
#* "\033[?25h"  <--- Show Cursor