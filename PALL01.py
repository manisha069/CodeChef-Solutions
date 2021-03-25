t=int(input())

for _  in range(t):
    ss=input()
    ls=[int(i) for i in ss]
    if ls==ls[::-1]:
        print("wins")
    else:
        print("loses")