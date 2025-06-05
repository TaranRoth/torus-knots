# Bredon Wood
def lens_genus(p: int, q: int):
    if p % 2 == 1 and q % 2 == 0:
        temp = p
        p = q
        q = temp
    if abs(p) == 2 and abs(q) == 1:
        return 1
    k = p / 2
    x = 2 * (k - q)
    a = None
    # q' = +-q % x
    if q % x <= k - q:
        a = q % x
    else:
       a = -q % x
    return lens_genus(x, a) + 1

# Teragaito
def get_n3genus(p: int, q: int):
    if abs(p) <= 1 or abs(q) <= 1:
        return 1
    temp_min, temp_max = min(p, q), max(p, q)
    p, q = temp_max, temp_min
    if (p * q) % 2 == 0:
        if p % 2 == 1 and q % 2 == 0:
            return lens_genus(q, p)
        return lens_genus(p, q)
    return lens_genus(p * q - 1, p ** 2)