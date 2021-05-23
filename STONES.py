t=int(input())
for _ in range(t):
    j=set(input())
    s=input()
    ss=[i for i in s]
    c=0
    for i in j:
        c+= ss.count(i)
    print(c)