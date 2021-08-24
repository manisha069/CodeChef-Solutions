t=int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    if ls.count(1)>=1 and ls.count(0)>=1:
        print(1)
    else:
        print(0)