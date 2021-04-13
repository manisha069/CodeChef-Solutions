t=int(input())
for _ in range(t):
    count=0
    n, k=map(int, input().split())
    ls=list(map(int, input().split()))
    ms=[i+k for i in ls]
    for i in ms:
        if i%7==0:
            count+=1
    print(count)