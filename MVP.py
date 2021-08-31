ds={}

t=int(input())
for _ in range(t):
    x =input()
    ds[x]=0
    ls=list(input().split())
    for i in ls:
        if i=="LOOT":
            ds[x] += 10
        elif i =="KILL":
            ds[x] += 50
        elif i =="REVIVE":
            ds[x] += 100
        elif i == "ASSIST":
            ds[x] += 30
m=max(ds.values())
for i in ds:
    if ds[i]==m:
        print(i)