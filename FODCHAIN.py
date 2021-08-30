t=int(input())
for _ in range(t):
    e, k = map(int, input().split())
    c=0
    while e!=0:
        e = e//k
        c+=1
    print(c)