# Fairchild
def get_arf(p: int, q: int):
    if q % 2 == 1:
        if p % 2 == 1 or q % 8 in [1, 7]:
            return 0 
        if p % 2 == 0 and q % 8 in [3, 5]:
            return 1
    if p % 2 == 1:
        return get_arf(q, p)
    return None

