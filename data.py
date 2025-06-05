import sqlite3 as sql


def get_invs(col_names):
    conn = sql.connect('knots.db')
    cursor = conn.cursor()
    conn.execute('BEGIN')
    data = list(cursor.execute(f'SELECT {", ".join(col_names)} FROM invariants'))
    conn.commit()
    conn.close()
    return data

get_invs(['p', 'q', 'arf'])