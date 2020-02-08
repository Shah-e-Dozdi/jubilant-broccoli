
from typing import Any
import math

def sphere_quadrant(x, y, z):
    if (0 <= x < math.inf) and (0 <= y < math.inf) and (0 < z < math.inf):
        result = "green"
    elif (0 <= x < math.inf) and (0 <= y < math.inf) and (-math.inf < z <= 0):
        result = "lower green"
    elif (0 <= x < math.inf) and (-math.inf < y < 0) and (0 < z < math.inf):
        result = "magenta"
    elif (0 <= x < math.inf) and (-math.inf < y < 0) and (-math.inf < z <= 0):
        result = "lower magenta"
    elif (-math.inf < x < 0) and (0 <= y < math.inf) and (0 < z < math.inf):
        result = "brown"
    elif (-math.inf < x < 0) and (0 <= y < math.inf) and (-math.inf < z <= 0):
        result = "lower brown"
    elif (-math.inf < x < 0) and (-math.inf < y < 0) and (0 < z < math.inf):
        result = "blue"
    elif (-math.inf < x < 0) and (-math.inf < y < 0) and (-math.inf < z <= 0):
        result = "lower blue"
    else:
        result = False
    return result