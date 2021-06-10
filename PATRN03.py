t=int(input())
for _ in range(t):
    n=int(input())
    for i in range(1, n+1):
        for j in range(1, i):
            print(str(j)+"*"*j, end="")
        print(str(i),  end="")
        print()