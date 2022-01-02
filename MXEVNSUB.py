t=int(input())
for _ in range(t):
    n=int(input())
    s = (n*(n+1))//2
    if s%2==0:
        print(n)
    else:
        print(n-1)