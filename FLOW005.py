t= int(input())
for _ in range(t):
    x=int(input())
    ans=0
    denom=[100,50,10,5,2,1]
    rem=x
    for i in denom:
        if (rem%i==0):
            ans=ans+(rem//i)
            break
        else:
            ans=ans+(rem//i)
            rem=rem%i
    print(ans)