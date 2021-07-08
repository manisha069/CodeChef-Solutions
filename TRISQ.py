t=int(input())
for _ in range(t):
    b = int(input())
    b -= 2
    b //= 2
    print((b*(b+1))//2)