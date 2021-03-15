t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if "I" in s:
        print("INDIAN")
    else:
        if "Y" not in s:
            print("NOT SURE")
        else:
            print("NOT INDIAN")