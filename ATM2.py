t=int(input())
for _ in range(t):
    ss=""
    n, tot = map(int, input().split())
    ls= list(map(int, input().split()))
    for i in ls:
        if tot- i>= 0:
            ss=ss+"1"
            tot=tot- i
        else:
            ss= ss+"0"
    print(ss)