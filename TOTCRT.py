t=int(input())
for _ in range(t):
    n= int(input())
    ds={}
    for _ in range(n*3):
        a, b = input().split()
        ds[a] = ds.get(a, 0)+int(b)
    
    ms = list(ds.values())
    ms.sort()
    print(*ms)