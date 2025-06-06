import sqlite3 as sql
import math
import sys
import pickle
from invs.signature import get_sig
from invs.upsilon import get_upsilon
from invs.arf import get_arf
from invs.d import get_d
from invs.alexander import display_alexander, get_alexander_blob
from invs.pinch import get_pinch
from invs.n3genus import get_n3genus
from lower import get_lowers
from upper import get_uppers

sys.setrecursionlimit(10000)
drop = True
p_limit = 64
invariant_presets = {
    'sig' : ('signature', get_sig, 'INTEGER'),
    'ups' : ('upsilon', get_upsilon, 'INTEGER'),
    'arf' : ('arf', get_arf, 'INTEGER'),
    'd' : ('d', get_d, 'INTEGER'),
    'alexander' : ('alexander', display_alexander, 'TEXT'),
    'pinch' : ('pinch', get_pinch, 'INTEGER'),
    'genus' : ('genus', lambda p, q: ((p - 1) * (q - 1)) / 2, 'INTEGER'),
    'bridge' : ('bridge', lambda p, q: min(abs(p), abs(q)), 'INTEGER'),
    'crossing' : ('crossing', lambda p, q: min(abs(p) * (abs(q) - 1), abs(q) * (abs(p) - 1)), 'INTEGER'),
    'unknotting' : ('unknotting', lambda p, q: ((p - 1) * (q - 1)) / 2, 'INTEGER'),
    'n3genus' : ('n3genus', get_n3genus, 'INTEGER'),
    'alexander_blob' : ('alexander_blob', get_alexander_blob, 'BLOB'),
}
# invariants = [invariant_presets['sig'], invariant_presets['ups'], invariant_presets['arf'], invariant_presets['d'], invariant_presets['alexander'], invariant_presets['pinch']]
invariants = [invariant for key, invariant in invariant_presets.items()]

def calculate_invs(cursor, invariants):
    for p in range(1, p_limit + 1):
        for q in range(1 , p + 1):
            if math.gcd(p, q) == 1:
                invs = tuple((invariant[1](p, q, cursor) if invariant[0] in ['alexander', 'alexander_blob'] else invariant[1](p, q) for invariant in invariants))
                lowers = get_lowers(p, q, invs)
                uppers = get_uppers(p, q, invs)
                bounds =  (max(lowers) if len(lowers) > 0 else None, min(uppers) if len(uppers) > 0 else None)
                fill_str = ("?," * (len(invariants) + 4))[:-1]
                cursor.execute(f'INSERT INTO invariants VALUES ({fill_str})', (p, q) + invs + bounds)
                """
                cursor.execute(f'INSERT INTO invariants VALUES ({fill_str})', (q, p) + invs + bounds)
                cursor.execute(f'INSERT INTO invariants VALUES ({fill_str})', (-p, -q) + invs + bounds)
                cursor.execute(f'INSERT INTO invariants VALUES ({fill_str})', (-q, -p) + invs + bounds)
                """


if __name__ == '__main__':
    conn = sql.connect('knots.db')
    cursor = conn.cursor()
    conn.execute('BEGIN')
    if drop == True:
        cursor.execute(f'DROP TABLE IF EXISTS invariants')
    inv_str = ''
    for invariant in invariants:
        inv_str += invariant[0] + f' {invariant[2]}, '
    inv_str = inv_str[:-2]
    cursor.execute(f'CREATE TABLE IF NOT EXISTS invariants(p INTEGER, q INTEGER, {inv_str}, lower INTEGER, upper INTEGER)')
    calculate_invs(cursor, invariants)
    conn.commit()
    conn.close()