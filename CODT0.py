t=int(input())
for _ in range(t):
    s=input()
    a=int(input())
    b= int(input())
    if s=='triangle':
        print(a*b)
    elif s == 'square':
        print((a*b)//2)
    elif s == 'rectangle':
        print(a*b)
    else:
        print(0)