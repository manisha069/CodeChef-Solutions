# cook your dish here
t=int(input())
for _ in range(t):
    n, m =map(int, input().split())
    a=list(map(int, input().split()))
    if len(set(a)) < m:
        print("Yes")
    else:
        print("No")