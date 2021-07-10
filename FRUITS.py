t=int(input())
for _ in range(t):
    n, m, k=map(int, input().split())
    for i in range(k):
        if n<m:
            n+=1
        elif n>m:
            m +=1
        else:
            break
    if n>m:
        print(n-m)
    elif m>n:
        print(m-n)
    else:
        print(0)