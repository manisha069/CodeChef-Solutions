t=int(input())
for _ in range(t):
    n = int(input())
    command = list(input().split())
    service = 0
    flag =0
    for i in command:
        if i =="start":
            service =1
        elif i=="restart":
            service = 1
        elif i =="stop":
            if service == 0:
                print("404")
                flag =1
                break
            else:
                service = 0
    if flag ==0:
        print("200")