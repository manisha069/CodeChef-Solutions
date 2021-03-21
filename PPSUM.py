def summ(n):
    x=0
    for i in range(1, n+1):
        x=x+i
    return x



t=int(input())
for _ in range(t):
    d, n = map(int, input().split())
    for i in range(d):
        n= summ(n)
    print(n)
    