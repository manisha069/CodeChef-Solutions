t=int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    s1=0
    s2=0
    for i in ls[0::2]:
        s1+= i
    for  i in ls[1::2]:
        s2+=i
    if s1==s2:
        print(0)
    elif s1>s2:
        print("1")
    else:
        print(2)
