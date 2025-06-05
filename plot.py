import sqlite3 as sql
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style='whitegrid', context='talk')


def scatter(cursor, condition, columns, coloring, p_limit):
    df = pd.DataFrame(cursor.execute(f'SELECT {columns} FROM invariants WHERE {condition} AND p <= {p_limit};'))
    df.columns = ['p', 'q']
    df[columns.split(',')] = pd.Series(dtype='str')
    plt.figure(figsize=(12, 9))
    for cond, color in coloring.items():
        color_knots = cursor.execute(f'SELECT p, q FROM invariants WHERE {cond} AND p < {p_limit};').fetchall()
        for knot in color_knots:
            df.loc[(df['p'] == knot[0]) & (df['q'] == knot[1]), 'color'] = color
    print(df.head())
    return sns.scatterplot(data = df, x='p', y='q', s = 1, marker = 'o',  edgecolor='black', hue='color')
    

def get_plot(cursor, function, title, condition, columns, coloring={'1:1':'steelblue'}, p_limit=1024):
    ax = function(cursor, condition, columns, coloring, p_limit)
    ax.set_title(title)
    ax.set_xlabel('p', fontsize=14)
    ax.set_ylabel('q', fontsize=14)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()
get_plot(cursor, scatter, 'Torus Knots with Nonorientable 4-genus 1', 'lower = 1 AND upper = 1', 'p,q', {'1=1':'steelblue'}, 1024)
get_plot(cursor, scatter, 'Torus Knots with Possible Nonorientable 4-genus 1', 'lower = 1', 'p,q', {'1=1' : 'steelblue', 'lower = upper' : 'red'}, 1024)
plt.show()
conn.close()