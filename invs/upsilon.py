from invs.signature import get_sig

#Fairchild
def get_upsilon(p: int, q: int):
    if p == 1 or p == -1 or q == 1 or q == -1:
        return 0
    if p == 2:
        return get_sig(p, q) / 2
    if p == -2:
        return get_sig(-p, -q) / 2
    temp_min, temp_max = min(p, q), max(p, q)
    p, q = temp_min, temp_max
    if p % 2 == 0:
        i = p / 2
        return get_upsilon(p, q - p) + (-i * (i + 1)) - (1/2 * p * (p - 1 - 2 * i))
    if (p - 1) % 2 == 0:
        i = (p - 1) / 2
        return get_upsilon(p, q - p) + (-i * (i + 1)) - (1/2 * p * (p - 1 - 2 * i))
    return get_upsilon(p, q - p) + get_upsilon(p, p + 1)


