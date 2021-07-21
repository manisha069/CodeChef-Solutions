t=int(input())
for _ in range(t):
    n = int(input())
    if n%10 ==0:
        print(n//10)
    else:
        print(n//10+1)