for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    e=[]
    o=[]
    for i in range(0,n):
        if l[i]%2==0:
            e.append(l[i])
        else:
            o.append(l[i])
            
    for i in range(0,len(e)):
        print(e[i],end=" ")
        
    for i in range(0,len(o)):
        print(o[i],end=" ")
    print()