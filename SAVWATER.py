t=int(input())
for _ in range(t):
    h, x,y,c= map(int, input().split())
    if (x+(y//2))*h <= c:
        print("YES")
    else:
        print("NO")