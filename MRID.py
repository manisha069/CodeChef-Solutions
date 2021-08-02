t=int(input())
for _ in range(t):
    n = int(input())
    ls =list(map(int, input().split()))
    if n >=5 :
        ls.sort()
        print(ls[-5])
    else:
        print(-1)