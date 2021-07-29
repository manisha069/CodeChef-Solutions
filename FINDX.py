t=int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    th=0
    for i in range(n-2):
        if ls[i]==3 and ls[i+2]==5:
            print(ls[i+1])
            th=1
            break
    if th==0:
        print(-1)