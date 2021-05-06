t=int(input())
for _ in range(t):
    ss= input()
    ls= set(ss)
    if len(ls)!=len(ss):
        print("NO")
    else:
        print("YES")