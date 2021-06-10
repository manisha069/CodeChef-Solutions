t=int(input())
for _ in range(t):
    x, m, d=map(int, input().split())
    print(min(x*m, x+d))