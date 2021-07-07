ls= [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
ls.reverse()
t=int(input())
for _ in range(t):
    c=0
    x=int(input())
    for i in ls:
        while x>=i:
            x-=i
            c+=1
           
    print(c)