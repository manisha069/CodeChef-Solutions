t=int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    print(max(ls)-min(ls))