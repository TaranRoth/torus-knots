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
    print(p, q)
    if abs(p) == 1 or abs(q) == 1:
        return 0
    q_inv = pow(q, -1, p)
    t = (-q_inv) % p
    u = pow(p, -1, q) % q
    return get_pinch(p - 2 * t, q - 2 * u) + 1

def find_preimage(p_start, q_start, hit_list=[], max_search=1000):
    for p_prev in range(2, max_search):
        for q_prev in range(2, max_search):
            try:
                q_inv = pow(q_prev, -1, p_prev)
                t = (-q_inv) % p_prev
                u = pow(p_prev, -1, q_prev) % q_prev

                p_candidate = p_prev - 2 * t
                q_candidate = q_prev - 2 * u

                if p_candidate == p_start and q_candidate == q_start:
                    hit_list.append((p_prev, q_prev))

            except ValueError:
                # Skip if inverse doesn't exist
                continue
    return sorted(hit_list, key=lambda x: x[0])

