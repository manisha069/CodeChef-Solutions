t=int(input())
for _ in range(t):
    s=input()
    if len(s)>=4:
        if s[0].isdigit():
            print(0)
        else:
            ls=s.split(" ")
            if len(ls)>1:
                print(0)
            else:
                ls=s.split("/")
                if len(ls)>1:
                    print(0)
                else:
                    num=0
                    cap=0
                    for i in s:
                        if i.isdigit():
                            num=1
                        if i.isupper():
                            cap=1
                    if num==cap==1:
                        print(1)
                    else:
                        print(0)
    else:
        print(0)