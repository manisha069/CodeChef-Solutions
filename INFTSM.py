t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    for i in range(1, n+1):
        ans += i*((i*2+1)**2)
    print(ans)