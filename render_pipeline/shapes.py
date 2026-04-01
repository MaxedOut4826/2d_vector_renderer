from . import Vector2, RenderParams, bezier

class Shape:
    render_queue: RenderParams = {"lines": [], "circles": []}
    
    @staticmethod
    def line(start: Vector2, end: Vector2) -> None:
        Shape.render_queue["lines"].append([start, end])
    
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
        w, h = size
        x0, y0 = start
        x1, y1 = x0 + w, y0 + h
        
        Shape.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
    
    @staticmethod
    def circle(centre: Vector2, radius: int) -> None:
        Shape.render_queue["circles"].append({
            'centre': centre,
            'radius': radius
        })
        
    @staticmethod
    def curve(points: list[Vector2]) -> None:
        resolution: int = 8
        
        vertices: list[Vector2] = []
        for i in range(0, resolution):
            t = i / (resolution - 1)
            
            vertices.append(bezier(t, points))
                
        Shape.polyline(vertices)



#! MUST ADD A 'PATH' METHOD TO CREATE A POLYLINE THAT ALLOWS CURVES 
#! MUST ADD TESSELLATION TO MAKE SHAPES FILLABLE WHICH ALLOWS FOR STROKE SIZE

#* Consider adding a 'move' method to displace a whole shape by a vector delta
#* Will need to store shapes differently though
#* The render queue should just take shapes from a shape catalogue
#* I can then also add methods like 'delete' for shapes and lines based on ID or index