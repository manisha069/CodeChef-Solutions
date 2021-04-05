t=int(input())
play=0
t1=0
t2=0
lead=0
for _ in range(t):
    a, b = map(int, input().split())
    t1=t1+a
    t2=t2+b
    x=abs(t1-t2)
    if x > lead:
        lead=x
        play=1 if a > b else 2
print(play, lead)