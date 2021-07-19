t=int(input())
for _ in range(t):
    s=input()
    if 'E' in s:
        if 'V' in s:
            if 'O' in s:
                if 'L' in s:
                    print("FOUND")
                else:
                    print("NOT FOUND")
            else:
                print("NOT FOUND")
        else:
            print("NOT FOUND")
    else:
        print("NOT FOUND")