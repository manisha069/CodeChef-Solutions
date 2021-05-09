# cook your dish here
t=int(input())
for _ in range(t):
    m, h =map(int, input().split())
    bmi = m//(h**2)
    if bmi <= 18:
        print(1)
    elif bmi>=19 and bmi<=24:
        print(2)
    elif bmi>=25 and bmi <=29:
        print(3)
    else:
        print(4)
        