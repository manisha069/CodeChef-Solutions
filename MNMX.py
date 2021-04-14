t=int(input())

for _ in range(t):
    n=int(input())
    ls=list(map(int, input().split()))
    if n==2:
        print(min(ls))
    else:
        print(min(ls)*(len(ls)-1))