"""
import sqlite3 as sql
import pickle

def check_alternating(poly):
    current_sign = poly[0][1]
    for term in poly[1:]:
        if term[1] not in [-1, 1]:
            print('WHAT!?!?!?!?!?!??!?!?!?!')
        sign = term[1]
        if sign == current_sign:
            return False
        current_sign = sign
    return True

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()
flag = True
length = len(list(cursor.execute('SELECT * FROM invariants')))
blobs = cursor.execute('SELECT alexander_blob FROM invariants')
for i in range(5):
    print(pickle.loads(blobs.fetchone()[0]))

for i in range(length):
    poly = pickle.loads(blobs.fetchone()[0])
    if not check_alternating(poly):
        flag = False
print(flag)

conn.close()
"""
"""
from invs.alexander import get_alexander
import math

t = 4
p = 63
q = None
for q in [8]:
    val = ((t ** (p * q) - 1) * (t - 1)) / ((t ** p - 1) * (t ** q - 1)) if math.gcd(p, q) == 1 else 1
    print(val % 4 ** 410)
"""





