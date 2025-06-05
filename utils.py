def fc_12(p: int, q: int):
    if q == 6:
        temp = p
        p = 6
        q = temp
    if p == 6 and q != 1:
        if q % 12 in [5, 7, 11]:
            return (2, 3)
        elif q % 12 == 1:
            if q % 5 == 0:
                return (2, 3)
            return (1, 3)
    return (0, None)

def fc_13(p: int, q: int):
    if q == 5:
        temp = p
        p = 5
        q = temp
    if p == 5:
        if q % 5 in [2, 3]:
            return (1, 1)
        if q % 10 in [4, 6, 9]:
            return (2, 2)
        if q % 10 == 1:
            return (1, 2)
    return (0, None)