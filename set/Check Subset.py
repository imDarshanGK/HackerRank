# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    test_case_a=int(input())
    a=set(map(int,input().split()))
    test_case_b=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))

