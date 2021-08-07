t=int(input())
for _ in range(t):
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[2]**2 == (ls[0]**2 +ls[1]**2) :
        print("RIGHT ANGLE TRIANGLE")
    else:
        print("NOT")