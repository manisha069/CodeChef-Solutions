import math
t=int(input())
for _ in range(t):

    n=int(input())
    x = int(math.sqrt(n))+1
    ls=[]
    for i in range(x):
        ls.append(2**i)
    ls.reverse()
    if n%2!=0:
        count=1
        n-=1
    else:
        count=0
    for i in ls:
            if i<=n:  
                n-=i
                count+=1
            else:pass
            if n==0:
                break
    print(count)