t=int(input())
for _ in range(t):
    sar=0
    anu=0
    xx="EQUINOX"
    n, a, b =map(int, input().split())
    for i in range(n):
        ss= input()
        if ss[0] in xx:
            sar+=a
        else:
            anu+=b
    if anu==sar:
        print("DRAW")
    elif sar>anu:
        print("SARTHAK")
    else:
        print("ANURADHA")