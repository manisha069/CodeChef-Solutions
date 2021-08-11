t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans=0
    for i in range(n, m+1):
        if i%3 !=0 and i%5!=0:
            ans+=i
    print(ans)