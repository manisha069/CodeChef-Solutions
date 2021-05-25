t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    x=n
    while x>0:
        if x%2 ==1:
            c+=1
        x=x//2
    print(c)