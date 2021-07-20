t=int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a+b+c==180:
            
        if a==b==c:
            print("EQUILATERAL")
        elif a==90 or b ==90 or c == 90:
            print("RIGHT")
        else:
            print("TRIANGLE")