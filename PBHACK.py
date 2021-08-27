yr=input()
n=int(input())
ans = []
ls=[]
for _ in range(n):
    ls.append(input())

for i in range(n):
    if set(ls[i]) == set(yr):
        ans.append(ls[i])

ans.sort()
print(*ans)