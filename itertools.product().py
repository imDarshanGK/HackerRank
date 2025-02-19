from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = product(a, b)

for item in result:
    print(f"({item[0]}, {item[1]})", end=" ")
