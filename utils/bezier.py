from . import Vector2

#De Casteljau's Algorithm
def bezier(t: float, coefs: list[Vector2]) -> Vector2:
    beta = coefs.copy()
    n = len(beta)
    
    for j in range(1, n):
        for k in range(n - j):
            x0, y0 = beta[k]
            x1, y1 = beta[k + 1]
            
            t0 = t
            t1 = 1 - t
            
            beta[k] = (
               round(x0 * t1 + x1 * t0),
                round(y0 * t1 + y1 * t0)
            )
            
    return beta[0]