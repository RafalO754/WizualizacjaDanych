import random

m=[[random.randint(0, 9) for j in range (0, 4, 1)] for i in range (0, 4, 1)]

p=[m[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]

print("Macierz 4x4:")

print(m[0])

print(m[1])

print(m[2])

print(m[3])

print("Przekątna: ",p)