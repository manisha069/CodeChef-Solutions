t=int(input())
for _ in range(t):
    n=int(input())
    ls = []
    for i in range(n):
        x=list(map(int, input().split()))
        ls.append(x)
    s1 = 0
    s2=0
    w=n-1
    for i in range(n):
        s1 +=ls[i][i]
        s2 += ls[i][w]
        w-=1
    print(abs(s1-s2))