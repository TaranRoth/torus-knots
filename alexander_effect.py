import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()
pd.DataFrame(cursor.execute('SELECT p, q, lower FROM invariants WHERE lower > 1')).to_csv('with_alexander.csv', index=False)
conn.close()
"""


with_alexander = pd.read_csv('with_alexander.csv')
without_alexander = pd.read_csv('without_alexander.csv')
diff = with_alexander.merge(without_alexander, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
diff.columns = ['p', 'q', 'lower']
diff.sort_values('lower')
print(diff)
sns.scatterplot(data=diff, x='p', y='q')
plt.show()
