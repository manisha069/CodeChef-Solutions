def ans(x):
    ss="abcdefghijklmnop"
    start=0
    mid =len(ss)//2
    end=len(ss)
    for i in x:
        if i=="0":
            end = mid
            mid = (start+end)//2
        else:
            start = mid
            mid = (start+end)//2
    print(ss[start:end], end="")




# x="1001"
t=int(input())
for _ in range(t):
    n=int(input())
    xx = input()
    if n==4:
        ans(xx)
        print()
    else:
        for i in range(0, n, 4):
            f = xx[i:i+4]
            ans(f)
        print()