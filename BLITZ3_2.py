t=int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print((2*(180+n))-(a+b))