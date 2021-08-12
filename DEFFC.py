t=int(input())
for _ in range(t):
    s =input()
    ls=[]
    for i in s:
        ls.append(int(i))
    print(max(ls)-min(ls))