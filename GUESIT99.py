# cook your dish here
t=int(input())
for _ in range(t):
    xx= int(input())
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    x=xx%7
    if x>7:
        days = days[x:]+days[:x]
        print(days[0])
    else:
        print(days[x])