t=int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    x = 60
    c=0
    ls.sort()
    for i in ls:
        if x-i>=0:
            x -= i
            c+=1
        else:
            break
    print(c)