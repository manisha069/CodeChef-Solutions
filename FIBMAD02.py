def fib(n):
    ls=[0, 1]
    f1=0
    f2=1
    temp=0
    for i in range(n):
        temp = f1
        f1= f2
        f2 = temp+ f1
        ls.append(f2)
    print(ls[n])

n=int(input())
fib(n)