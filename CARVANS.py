t=int(input())
for _ in range(t):
    n=int(input())
    ls=list(map(int, input().split()))
    if n==1:
        print(1)
    else:
        c=1
        f=ls[0]
        for i in range(1, n):
            if ls[i]<f:
                f=ls[i]
                c+=1
        print(c)