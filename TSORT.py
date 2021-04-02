n=int(input())
ls=[]
for _ in range(n):
    x=int(input())
    ls.append(x)
ls.sort()
for i in ls:
    print(i)