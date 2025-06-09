from utils import get_conn_cursor
import pandas as pd

cursor, conn = get_conn_cursor('knots.db')

data = pd.DataFrame(cursor.execute('SELECT upper - lower FROM invariants'))
print(data.value_counts())

conn.close()