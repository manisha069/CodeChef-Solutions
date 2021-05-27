ss = "abcdefghijklmnopqrstuvwxyz"
t=int(input())
for _ in range(t):
    xx=input()
    s=0
    for i in xx:
        s+= ss.index(i)+1
    if s%2==0:
        print("YES")
    else:
        print("NO")