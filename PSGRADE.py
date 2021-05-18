t= int(input())
for _ in range(t):
    ls=list(map(int, input().split()))
    amin=ls[0]
    bmin = ls[1] 
    cmin = ls[2]
    tmin = ls[3] 
    a = ls[4] 
    b = ls[5] 
    c = ls[6]

    if a>=amin and b>=bmin and c>=cmin:
        if (a+b+c)>=tmin:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")