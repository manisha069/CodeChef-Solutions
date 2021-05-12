m=int(input())
ar=list(map(int, input().split()))
n=int(input())
for i in range(n):
    pos=int(input())
    print(ar.pop(pos-1))