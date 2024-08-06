if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=set(arr)
    score = sorted(a)
    runner_up=score[-2]
    print(runner_up)
    
    
