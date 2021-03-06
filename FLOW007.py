def rev(k):
    y=0
    while k>0:
        y=(y*10)+(k%10)
        k=k//10
        
    print(y)

t=int(input())
for _ in range(t):
    x=int(input())
    rev(x)