t=int(input())
for _ in range(t):
    n, k=map(int, input().split())
    ls=list(map(int, input().split()))
    ls.sort()
    k=min(k, n-k)
    a=sum(ls[:k])
    b = sum(ls[k:])
    print(b-a)