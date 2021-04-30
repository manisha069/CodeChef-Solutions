# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    ls = list(map(int, input().split()))
    x = int(input())
    xval = ls[x-1]
    ls.sort()
    print(ls.index(xval)+1)