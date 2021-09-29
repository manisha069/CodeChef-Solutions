import math
t=int(input())
for _ in range(t):
    n, a =map(int, input().split())
    print(int(math.sqrt(n))*a)