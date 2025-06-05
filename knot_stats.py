import sqlite3 as sql
import pandas as pd

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()

def pct_limit(cursor, condition: str, p_limit: int):
    return cursor.execute(f'SELECT ROUND(100.0 * AVG(CASE WHEN {condition} THEN 1 ELSE 0 END), 2) FROM invariants WHERE p <= {p_limit}').fetchone()[0]


data = []
for p_limit in [2 ** n for n in range(4, 14)]:
    k1 = pct_limit(cursor, 'lower = 1 AND upper = 1', p_limit)
    k = pct_limit(cursor, 'lower = upper', p_limit)
    n1 = pct_limit(cursor, 'lower > 1', p_limit)
    nk = pct_limit(cursor, 'lower = 1 AND upper > 1', p_limit)
    data.append([k1, k, n1, nk])

df = pd.DataFrame(data=data, columns=('k1', 'k', 'n1', 'nk'))
df.to_csv('knot_stats.csv')

cursor.close()