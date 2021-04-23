t=int(input())
for _ in range(t):
    ss=input()
    aa=ss.count("a")
    bb=ss.count("b")
    if aa == bb:
        print(aa)
    elif aa ==0:
        print(0)
    elif bb == 0:
        print(0)
    elif aa>bb:
        print(bb)
    else:
        print(aa)