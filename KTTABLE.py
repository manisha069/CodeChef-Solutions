t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    slot=list(map(int, input().split()))
    time=list(map(int, input().split()))
    if slot[0]>=time[0]:
        count += 1
    for i in range(1, len(slot)):
        t=slot[i] - slot[i-1]
        if t>= time[i]:
            count+=1
    print(count)