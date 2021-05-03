t=int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ai = list(map(int, input().split()))
    for j in range(n):
        s=input()
        tot=0
        for i in range(len(s)):
            if s[i]=="1":
                tot+= ai[i]
        print(tot)
        