from numpy.polynomial import Polynomial
import numpy as np
import pickle 

def get_unsimplified_poly(n):
        coeffs = [0] * (n + 1)
        coeffs[0] = 1
        coeffs[n] = -1
        return Polynomial(coeffs)

def get_alexander(p: int, q: int, cursor):
    disregard_alexander = False
    if disregard_alexander:
        return [(0, 1)]

    cache_flag = False
    if cache_flag:
        cursor.execute(f'SELECT alexander_blob FROM alexander_backup WHERE p = {p} AND q = {q}')
        cached_poly = pickle.loads(cursor.fetchone()[0])
        return cached_poly

    num = get_unsimplified_poly(p * q) * get_unsimplified_poly(1)
    den = get_unsimplified_poly(p) * get_unsimplified_poly(q)

    quot, rem = divmod(num, den)

    quot = Polynomial([round(c) for c in quot.coef])

    coeffs = np.round(quot.coef).astype(int)
    deg = np.max(np.nonzero(coeffs))
    pows = np.arange(len(coeffs)) - (deg // 2)
    poly = [(power, coeff) for power, coeff in zip(pows, coeffs) if coeff != 0]
    return list(map(lambda term: (int(term[0]), int(term[1])), poly))

     
def display_alexander(p: int, q: int, cursor):
    poly = get_alexander(p, q, cursor)
    poly_str = ''
    first_flag = True
    for term in poly:
        if term[1] == 1 and term[0] != 0:
            if first_flag:
                term = (term[0], '')
            else:
                term = (term[0], '+')
        if term[1] == -1 and term[0] != 0:
            term = (term[0], '-')
        if term[0] == 0:
            poly_str += str(term[1])
        else:
            poly_str += str(term[1]) + 't^' + str(term[0])
        first_flag = False
    return poly_str

def get_alexander_blob(p: int, q: int, cursor):
    return pickle.dumps(get_alexander(p, q, cursor))

