t=int(input())
for _ in range(t):
    n=int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    ls.reverse()
    c=0
    f=0
    for i in ls:
        if i%5==0:
            c+=1
        if c==3:
            print(i)
            f=1
            break
    if f==0:
        print(-1)