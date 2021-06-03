t=int(input())
for _ in range(t):
    D, d, a, b, c = map(int, input().split())
    tot = d*D
    if tot <10:
        print(0)
    elif tot>=10 and tot<21:
        print(a)
    elif tot >=21 and tot <42:
        print(b)
    elif tot>=42:
        print(c)