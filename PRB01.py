t=int(input())
for _ in range(t):
    n= int(input())
    if n==1:
        print("no")
    elif n==2:
        print("yes")
    elif n%2==0 and n!=2:
        print("no")
    else:
        for i in range(3, n, 2):
            if n%i==0:
                print("no")
                break
        else:
            print("yes")