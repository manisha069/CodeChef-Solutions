n, m=map(int, input().split())
ls = list(map(int, input().split()))
maxu=0
for i in range(n-m):
    xx = set(ls[i:i+m])
    if len(xx) > maxu:
        maxu = len(xx)
print(maxu)