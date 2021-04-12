t=int(input())
for _ in range(t):
    x=input()
    ls=[int(i) for i in x]
    zeros= ls.count(0)
    ones = ls.count(1)
    if zeros==1 or ones==1:
        print("Yes")
    else:
        print("No")