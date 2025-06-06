import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np
import sqlite3 as sql

conn = sql.connect('knots.db')
conn.execute('BEGIN')
cursor = conn.cursor()

data = torch.tensor(cursor.execute('SELECT p, q, signature, upsilon, d, pinch, genus, n3genus, lower FROM invariants').fetchall())
conn.close()

device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else 'cpu'

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)

X = data# [:, :-1]
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(y_pred)