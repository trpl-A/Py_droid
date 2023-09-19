# CLASS FOR THE VOLUME OF A SHAPE
# ===============================

import math 

class Shape:
    def v_box(l=float, w=float, h=float):
        v = l * w * h

    def v_tri_prism(l, w, h):
        v = (l * w * h) / 2
        return v

    def v_square_pyramid(l, w, h):
        v = (l * w * h) / 3
        return v 
    # ===================================

    def v_sphere(r):
        pi = math.pi 
        # pi = 3.1452
        v = (4/3) *  pi * (r ** 3)
        return v

    def v_cylinder(r, h):
        pi = math.pi
        # pi = 3.1452
        v = pi * (r ** 2) * h
        return v
    
    def v_cone(r, h):
        pi = math.pi 
        # pi = 3.1452
        v = (pi * (r ** 2) * h) / 3
        return v 
    
# ****************************************