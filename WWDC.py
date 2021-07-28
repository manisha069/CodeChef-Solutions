t=int(input())
for _ in range(t):
    n, k = map(int,input().split())
    ls = list(map(int, input().split()))
    ls.sort()
    c=0
    for i in ls:
        if i>=k:
            c+=1
    print(c)