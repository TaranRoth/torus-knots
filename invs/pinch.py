# Fairchild
def pinch_condition(p: int, q: int):
    condition_val = p > 3 and (q % (2 * p) in [(p - 1) % (2 * p), (p + 1) % (2 * p), (2 * p + 1) % (2 * p)])
    if p < q:
        return condition_val or pinch_condition(q, p)
    return condition_val

"""
def get_pinch(p: int, q: int):
    if p > q:
        return get_pinch(q, p)
    if p > 3:
        if p % 2 == 1:
            if q % (2 * p) == (p - 1) % (2 * p):
                return (p - 1) / 2
            if q % (2 * p) in [(p + 1) % (2 * p), (2 * p - 1) % (2 * p)]:
                return (p - 1) / 2
        else:
            if q > p and (q % (2 * p) in [(p - 1) % (2 * p), (p + 1) % (2 * p), (2 * p + 1) % (2 * p)]):
                return p / 2
    return None
"""
# Sabloff
def get_pinch(p: int, q: int):
    if abs(p) == 1 or abs(q) == 1:
        return 0
    q_inv = pow(q, -1, p)
    t = (-q_inv) % p
    u = pow(p, -1, q) % q
    return get_pinch(p - 2 * t, q - 2 * u) + 1

