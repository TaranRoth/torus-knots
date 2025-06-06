import torch
import numpy as np
import sqlite3 as sql

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()

print(torch.rand(5, 3))

conn.close()