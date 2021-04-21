t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    ls=list(map(int, input().split()))
    if k ==1:
        print(0)
    else:
        ls.sort()
        diff=0
        minn = max(ls)
        for i in range(n-k+1):
            a= ls[i+k-1]
            b= ls[i]

            diff = a-b
            if diff < minn:
                minn=diff
        print(minn)   