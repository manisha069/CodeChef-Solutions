t=int(input())
for _ in range(t):
    n, s = map(int, input().split())
    ans =0
    for i in range(1, n*2, 2):
        ans +=i
    print(ans-s)