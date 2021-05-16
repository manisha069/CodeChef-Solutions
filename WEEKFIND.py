# cook your dish here
t=int(input())
for _ in range(t):
    ls=input().split()
    ls[1] = int(ls[1])
    ss=ls[0]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    x=ls[1]%7
    y=days.index(ss)
    if y!=0:
        days = days[y:]+days[:y]
        print(days[x])
    else:
        print(days[x])