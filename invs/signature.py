# Fairchild
def get_sig_unsigned(p: int, q: int):
    temp_max = max(p, q)
    temp_min = min(p, q)
    p = temp_max
    q = temp_min
    if q == 1 or q == 0:
        return 0
    if q == 2:
        return p - 1
    if 2 * q < p:
        if q % 2 == 1:
            return get_sig_unsigned(p - 2 * q, q) + q ** 2 - 1
        return get_sig_unsigned(p - 2 * q, q) + q ** 2
    if q <= p < 2 * q:
        if q % 2 == 1:
            return q ** 2 - 1 - get_sig_unsigned(2 * q - p, q)
        return q ** 2 - 2 - get_sig_unsigned(2 * q - p, q)
    return q ** 2 - 1

def get_sig(p: int, q: int):
    if p < 0 and q > 0:
        return get_sig_unsigned(-p, q)
    if q < 0 and p > 0:
        return get_sig_unsigned(p, -q)
    if q < 0 and p < 0:
        return -get_sig_unsigned(-p, -q)
    return -get_sig_unsigned(p, q)


