t= int(input())
for  _ in range(t):
    ls=list(map(int, input().split()))
    ls.sort()
    if ls[0]==ls[1] and ls[-1]==ls[-2]:
        print("YES")
    else:
        print("NO")