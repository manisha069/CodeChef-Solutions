n, x =map(int, input().split())
a = list(map(int, input().split()))
if sum(a)+x<=25:
    print("YES")
else:
    print("NO")