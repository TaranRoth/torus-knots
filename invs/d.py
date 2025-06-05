import math

# Fairchild
def get_d(p: int, q: int):
    temp_max = max(p, q)
    temp_min = min(p, q)
    p = temp_min
    q = temp_max
    p_fl = math.floor(p / 2)
    s = 0
    for i in range(0, p_fl):
        s += math.floor(((p - 1 - (2 * i)) * q - p - 1) / (2 * p))
    return 2 * (p_fl + s)
