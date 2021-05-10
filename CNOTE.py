# cook your dish here
t=int(input())
for _ in range(t):
    x, y, k, n = map(int, input().split())
    if y <x:
        flag=0
        x-=y
        for i in range(n):
            if flag==0:
                pg, amt = map(int, input().split())
                if amt <=k and pg>=x:
                    print("LuckyChef")
                    flag=1
            else:
                jk, j=kj=map(int, input().split())
        if flag==0:
            print("UnluckyChef")
        
    else:
        print("LuckyChef")