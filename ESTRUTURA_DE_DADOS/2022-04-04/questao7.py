# 7. (Matriz) Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e
# somar todos os elementos da matriz = np.array([[3, 4, 1], [3, 1, 5]]).

import numpy as np

matriz = np.array([[3, 4, 1], [3, 1, 5]])
sun = 0

for column in matriz:
    for row in column:
        sun += row


print(f"soma da matriz = {sun}")