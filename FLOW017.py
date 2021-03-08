t=int(input())
for _ in range(t):
    x=list(map(int, input().split()))
    x.sort()
    print(x[1])