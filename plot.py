import sqlite3 as sql
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd
from modulo import find_lines
from utils import get_conn_cursor

sns.set_theme(style='whitegrid', context='talk')


def scatter(cursor, condition, columns, coloring, default_color, p_limit):
    df = pd.DataFrame(cursor.execute(f'SELECT {columns} FROM invariants WHERE {condition} AND p <= {p_limit};'))
    df.columns = ['p', 'q']
    df['color'] = pd.Series(dtype='str')
    plt.figure(figsize=(12, 9))
    for cond, color in coloring.items():
        color_knots = cursor.execute(f'SELECT p, q FROM invariants WHERE {cond} AND p < {p_limit};').fetchall()
        for knot in color_knots:
            df.loc[(df['p'] == knot[0]) & (df['q'] == knot[1]), 'color'] = color
    df['color'] = df['color'].fillna(default_color)
    size_mapping = {'red' : 1, 'green' : 5}
    df['size'] = df['color'].map(size_mapping)
    #return sns.scatterplot(data = df, x='p', y='q', size='size', marker = 'o',  edgecolor='black', hue='color', palette={**{default_color:default_color}, **{color:color for cond, color in coloring.items()}})
    return sns.scatterplot(data = df, x='p', y='q', s=1, marker = 'o',  edgecolor='black', hue='color', palette={**{default_color:default_color}, **{color:color for cond, color in coloring.items()}})

def heatmap(cursor=get_conn_cursor('knots.db')[1], filt='1=1', grad_var='lower', columns='p,q', low_color='blue', high_color='red', p_limit=1024):
    df = pd.DataFrame(cursor.execute(f'SELECT {columns}, {grad_var} FROM invariants WHERE p < {p_limit} AND {filt}'))
    df.columns = columns.split(',') + [grad_var]
    cmap = sns.color_palette([low_color, high_color], as_cmap=True)
    return sns.heatmap(df, x='p', y='q', cmap=cmap)

def plot_lines(ax, slopes, p_limit, color='blue', linestyle='--', linewidth=3):
    for m in slopes:
        x_vals = [0, p_limit]
        y_vals = [m * x for x in x_vals]
        ax.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=linewidth, label=f'q={m}p')

def get_plot(cursor, plot, title, condition, columns, coloring={}, coloring_labels={}, p_limit=1024, default_color='red', default_label='Default'):
    ax = None
    if plot == scatter:
        ax = plot(cursor, condition, columns, coloring, default_color, p_limit)
    if plot == heatmap:
        ax = plot(filt=condition, columns=','.join(columns.split(',')[:-1]), grad_var=columns.split(',')[-1])
    ax.set_title(title)
    ax.set_xlabel('p', fontsize=14)
    ax.set_ylabel('q', fontsize=14)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.tight_layout()
    # Move to scatter function
    """
    legend_patches = []
    legend_patches.append(mpatches.Patch(color=default_color, label='Possible Gamma=1'))
    for cond, label in coloring_labels.items():
        legend_patches.append(mpatches.Patch(color=coloring[cond], label=label))
    if legend_patches:
        plt.legend(handles=legend_patches, loc='best', fontsize=12)
    plot_lines(ax, find_lines(1024).keys(), 1024)
    """



if __name__ == '__main__':
    conn = sql.connect('knots.db')
    conn.execute('BEGIN')
    cursor = conn.cursor()
    p_limit = 1024
    # get_plot(cursor, scatter, 'Torus Knots with Nonorientable 4-genus 1', 'lower=1 AND upper=1', 'p,q', {}, {}, p_limit, 'red', 'Gamma=1')
    # get_plot(cursor, scatter, 'Torus Knots with Possible Nonorientable 4-genus 1', 'lower=1', 'p,q', {'lower=upper' : 'green'}, {'lower=upper' : 'Known Gamma=1'}, p_limit, 'red', 'Possible Gamma=1')
    get_plot(cursor, heatmap, 'Torus Knots by Lower Bound on Nonorientable 4-Genus', 'lower=1', 'p,q,lower')
    plt.show()
    conn.close()