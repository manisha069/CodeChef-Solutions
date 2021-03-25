t=int(input())
for _ in range(t):
    ss=input()
    x=len(ss)//2
    a=[]
    b=[]
    if len(ss)%2==0:
        for i in range(0, x):
            a.append(ss[i])
            b.append(ss[i+x])
   
    
    else:   
        for i in range(0, x+1):
            a.append(ss[i])
            b.append(ss[i+x])
        
    
    a.sort()
    b.sort()

    for i in range(len(a)):
        if a[i]!=b[i]:
            print("NO")
            break
    else:
        print("YES")