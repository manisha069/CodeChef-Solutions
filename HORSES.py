t=int(input())
for _ in range(t):
    n=int(input())
    ls= list(map(int, input().split()))
    ls.sort()
    m=ls[-1]
    for i in range(len(ls)-1):
        if (ls[i+1]-ls[i]) < m:
            m = ls[i+1]-ls[i]
    print(m)