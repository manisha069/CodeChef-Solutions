t=int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = a+b
    if x<3:
        print(1)
    elif x >=3 and x<= 10:
        print(2)
    elif x >= 11 and x<=60:
        print(3)
    else:
        print(4)
    