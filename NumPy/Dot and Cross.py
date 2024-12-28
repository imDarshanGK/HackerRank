import numpy as np

X = int(input())
A = np.array([list(map(int, input().split())) for _ in range(X)])
B = np.array([list(map(int, input().split())) for _ in range(X)])

result = np.dot(A, B)

print(result)
