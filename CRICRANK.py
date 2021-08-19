t=int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    bs =  list(map(int, input().split()))
    a=0
    b=0
    for i in range(3):
        if ls[i]>bs[i]:
            a+=1
        else:
            b+=1
    if a>b:
        print("A")
    else:
        print("B")