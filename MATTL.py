t=int(input())
for _ in range(t):
    l, r = map(int, input().split())
    c=0
    for i in range(l, r+1):
        if i%2==0:
            c+=1
       
    if c%2==0 :
        print("PASS")
    else:
        print("FAIL")