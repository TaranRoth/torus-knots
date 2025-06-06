import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore

# Example DataFrame
conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()

df = pd.DataFrame(cursor.execute('SELECT p, q, lower, upper FROM invariants'))
df.columns = ['p', 'q', 'lower', 'upper']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vertical lines from lower_bound to upper_bound
for _, row in df.iterrows():
    ax.plot(
        [row['p'], row['p']],          # x values (constant)
        [row['q'], row['q']],          # y values (constant)
        [row['lower'], row['upper']],  # z values
        color='b'
    )

# Optionally add scatter points at ends of the lines
ax.scatter(df['p'], df['q'], df['lower'], color='r', label='Lower Bound')
ax.scatter(df['p'], df['q'], df['upper'], color='g', label='Upper Bound')

# Labels and title
ax.set_xlabel('p')
ax.set_ylabel('q')
ax.set_zlabel('Bounds')
ax.set_title('3D Scatterplot with Bounds')

# Add legend
ax.legend()

# Show plot
plt.show()