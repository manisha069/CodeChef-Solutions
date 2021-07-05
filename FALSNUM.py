t=int(input())
for _ in range(t):
    n=input()
    if int(n[0])==1:
        print(n[0]+"0"+n[1:])
    elif int(n[0])>1:
        print('1'+n[0:])
    else:
        print('1'+n[0:])