m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

symmetric_difference = sorted(a.symmetric_difference(b))
for value in symmetric_difference:
    print(value)
