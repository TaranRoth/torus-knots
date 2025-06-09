from utils import get_conn_cursor

def check_line(slope, mult, p, q, data):
    return True

def get_lines():
    cursor, conn = get_conn_cursor('knots.db')
    data = list(cursor.execute('SELECT p, q FROM invariants WHERE lower = 1 AND upper = 1'))
    print(data)


    conn.close()

if __name__ == '__main__':
    get_lines()