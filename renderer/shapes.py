from . import Vector2, RenderParams

class Shape:
    render_queue: RenderParams = {"lines": [], "circles": []}
    
    @staticmethod
    def line(start: Vector2, end: Vector2) -> None:
        Shape.render_queue["lines"].append({
                'start': start,
                'end': end
            })
    
    @staticmethod
    def polyline(lines: list[Vector2]) -> None:
        if len(lines) < 2:
            return print("Not Enough Arguments Given for Polyline")
        
        for start, end in zip(lines, lines[1:]):
            Shape.line(start, end)
        
    @staticmethod
    def polygon(lines: list[Vector2]) -> None:
        lines.append(lines[0])
        Shape.polyline(lines)
            
    @staticmethod
    def rect(start: Vector2, size: Vector2) -> None:
        x0, y0 = start
        x1, y1 = x0 + size[0], y0 + size[1]
        
        Shape.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
    
    @staticmethod
    def circle(centre: Vector2, radius: int) -> None:
        Shape.render_queue["circles"].append({
            'centre': centre,
            'radius': radius
        })


#! MUST ADD A BEZIER CURVES METHOD / OPTIONAL LINE PARAMETER (PROBS THE LATTER); USES 'De Casteljau's Algorithm TO SUBDIVIDE LINES 
