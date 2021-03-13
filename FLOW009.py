t=int(input())
for _ in range(t):
    q, p = map(float, input().split())
    if q>1000:
        tot=q*p
        dis=tot/10
        tot=tot-dis
        print(tot)
    else:
        print(q*p)