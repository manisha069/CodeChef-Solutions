n, k=map(int, input().split())
cc=0
for _ in range(n):
    x=int(input())
    if x%k==0:
        cc+=1
print(cc)