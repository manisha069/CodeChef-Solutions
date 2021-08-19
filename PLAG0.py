t=int(input())
for _ in range(t):
    n=int(input())
    ls = list(map(int, input().split()))
    if max(ls)>=80:
        print("BANNED")
    elif max(ls)<80 and max(ls)>=60:
        print("PLAGIARISED -275")
    else:
        print("COINCIDENCE")