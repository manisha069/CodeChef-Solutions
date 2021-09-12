t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    while n!=0:
        if n%2==0:
            n=n//2
            c+=1
        else:
            n-=1
            c+=1
    print(c)