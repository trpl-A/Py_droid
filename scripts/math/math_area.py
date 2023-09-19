# CLASS FOR AREA-OF-A-2D-SHAPE CALCULATIONS
# =========================================

import math

class Shapes:
    def a_rect(length, breadth):
        a = length * breadth
        return a

    def a_triangle(base, height):
        a = 1/2 * (base * height)
        return a 
    
    def a_circle(r):
        pi = math.pi
        # pi = 3.1452
        a = pi * (r ** 2)
        return a 

    def a_oval(maj_r, min_r):
        pi = math.pi
        # pi = 3.1452
        a = pi * (maj_r * min_r) 
        return a 
    
# *******************************