t=int(input())
for _ in range(t):
    n=int(input())
    ls=list(map(int, input().split()))
    ss=set(ls)
    for i in ss:
        if ls.count(i)==1:
            print(i)