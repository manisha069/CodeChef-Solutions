t=int(input())
for _ in range(t):
    n, k =map(int, input().split())
    ls=[]
    for i in range(1, k+1):
        ls.append(n%i)
    print(max(ls))