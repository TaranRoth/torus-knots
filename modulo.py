from utils import get_conn_cursor
import math
from fractions import Fraction

def check_line(slope, mult, p, q, data):
    return True

def find_lines(p_limit: int):
    cursor, conn = get_conn_cursor('knots.db')
    data = list(cursor.execute('SELECT p, q FROM invariants WHERE lower=1 AND upper=1'))
    data = list(filter(lambda x: x[0] > 100, data))
    lines = {}
    for p, q in data:
        matched = False
        slope = q / p
        for rep_slope, knots in lines.items():
            if abs(slope - rep_slope) < .05:
                matched = True
                knots.append((p, q))
        if not matched:
            lines[slope] = [(p, q)]
    print(len(data), len(lines))
    for slope, knots in lines.items():
        print(knots)

    conn.close()
    return lines


def get_density(data, p, q, radius):
    counter = 0
    for knot in data:
        if math.sqrt((knot[0] - p) ** 2 + (knot[1] - q) ** 2) <= radius:
            counter += 1
    total = 0
    

def find_breaks(p_limit: int, p_range: int=10, min_range: int=10, max_range: int=100):
    conn, cursor = get_conn_cursor('knots.db')
    data = list(cursor.execute(f'SELECT p, q FROM invariants WHERE lower=1 AND p<{p_limit} AND p>{p_limit - 10}'))
    print(data)
    for increment in range(min_range, max_range + 1):
        pass

if __name__ == '__main__':
    # lines = find_lines(1024)
    slopes = find_lines(1024).keys()
    

    
