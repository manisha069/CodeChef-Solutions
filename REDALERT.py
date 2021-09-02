t=int(input())
for _ in range(t):
    n, d, h= map(int,input().split())
    ls = list(map(int, input().split()))
    lev=0

    for i in ls:
        if i ==0:
            if lev < d:
                lev =0
            else:
                lev -= d
        else:
            lev += i
        if lev > h:
            print("YES")
            break
 
    else:
        print("NO")
            