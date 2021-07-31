t=int(input())
for _ in range(t):
        n = int(input())
        ls = list(map(int, input().split()))
        if ls.count(0)>=1:
            print("NO")
        else:
            print("YES")