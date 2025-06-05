import sqlite3 as sql
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style='whitegrid', context='talk')


def scatter(cursor, condition, columns, coloring):
    df = pd.DataFrame(cursor.execute(f'SELECT {columns} FROM invariants WHERE {condition}'))
    color_dfs = []
    for cond, color in coloring.items():
        (color_dfs.append(pd.DataFrame(cursor.execute(f'SELECT {columns} FROM invariants WHERE {cond}'))), color)
    df.columns = ['p', 'q']
    plt.figure(figsize=(12, 9))
    clrs = []
    for row in df:
        for cond, color in coloring.items():
            if len(list(cursor.execute(f'SELECT * FROM invariants WHERE p={row['p']} AND q={row['q']} AND {condition}'))) > 1:
                clrs.append(color)
                continue
    df['colors'] = clrs
    return sns.scatterplot(data = df, x='p', y='q', s = 100, marker = 'o',  edgecolor='black', hue='category', palette=df['colors'])
    

def get_plot(cursor, function, title, condition, columns, coloring):
    ax = function(cursor, condition, columns, coloring)
    ax.set_title(title)
    ax.set_xlabel('p', fontsize=14)
    ax.set_ylabel('q', fontsize=14)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()
get_plot(cursor, scatter, 'Torus Knots with Nonorientable 4-genus 1', 'lower = 1 AND upper = 1', 'p, q', {})
get_plot(cursor, scatter, 'Torus Knots with Possible Nonorientable 4-genus 1', 'lower = 1', 'p, q', {'lower = upper' : 'red'})
plt.show()
conn.close()