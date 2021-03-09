t= int(input())
for _ in range(t):
    h, c, t = map(float, input().split())
#     print(h, c, t)
    if (h> 50.0 and c<0.7 and t > 5600.0):
        print(10)
    elif (h >50.0 and c< 0.7):
        print(9)
    elif (c< 0.7 and t> 5600.0):
        print(8)
    elif (h > 50.0 and t> 5600.0):
        print(7)
    elif (h > 50.0  or c < 0.7 or t > 5600.0):
        print(6)
    else:
        print(5)