t=int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int,input().split()))
    s =set(ls)
    g=0
    for i in s:
        if ls.count(i)==1:
            if i%2!=0:
                print("PASS")
                g=1
            
    if g==0:
        print("FAIL")