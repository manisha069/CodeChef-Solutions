t=int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(2)
    else:
        ans=2
        for i in range(1,n):
            ans += ((i*10)+1)
        print(ans)