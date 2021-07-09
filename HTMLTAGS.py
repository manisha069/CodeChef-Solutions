t=int(input())
for _ in range(t):
    s = str(input())
    if s[:2]=="</":
        if s[-1]=='>':
            x = s[2:-1]
            if x.isalnum() and x.islower():
                print("Success")
            elif x.isdigit():
                print("Success")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("Error")
