import sqlite3 as sql
from numpy.polynomial import Polynomial
import numpy as np

"""
def get_alexander(p: int, q: int):
    t = sym.Symbol('t')
    num = (t ** (p * q) - 1) * (t - 1) 
    den = (t ** p - 1) * (t ** q - 1)
    ply = sym.expand(sym.simplify(num / den))
    exp = [term.as_coeff_exponent(t)[1] for term in ply.as_ordered_terms()]
    laurent = sym.powsimp(sym.expand(ply * (t ** (-(max(exp) + min(exp)) // 2)), power_exp=True), force=True)
    return str(laurent)
"""
def get_unsimplified_poly(n):
        coeffs = [0] * (n + 1)
        coeffs[0] = 1
        coeffs[n] = -1
        return Polynomial(coeffs)

def get_alexander(p: int, q: int, cursor):
    cache_flag = False
    if cache_flag:
        cached_poly = list(cursor.execute(f'SELECT alexander FROM invariants WHERE p = {p}, q = {q}'))
        if len(cached_poly) > 0:
             print(cached_poly)

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
    for term in poly:
        if term[1] == 1:
            term[1] = '+1'
        if term[0] == 0:
            poly_str += str(term[1])
        else:
            poly_str += str(term[1]) + 't^' + str(term[0])
    return poly_str

