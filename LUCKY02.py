t=int(input())
for _ in range(t):
    c= input()
    x=[int(i) for i in c]
#     print("list", s)
    s=[{3}, {7}, {3,7}, {7,3}]
    setc = set(x)
#     print("setc", setc)
    if setc in s:
        print("LUCKY") 
    else:
        print("BETTER LUCK NEXT TIME")