t=int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    if n%2==1:
        a*=2
    print(max(a, b)//min(a, b))