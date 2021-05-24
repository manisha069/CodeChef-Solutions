t=int(input())
for _ in range(t):
    x, a, b=map(int, input().split())
    print(10*(a+(100-x)*b))