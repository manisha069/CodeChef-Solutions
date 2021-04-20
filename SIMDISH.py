t=int(input())
for _ in range(t):
    done = list(input().split())
    dtwo = list(input().split())
    setone = set(done)
    setwo = set(dtwo)
    z= setone.intersection(setwo)
    if len(z) >= (len(done)//2):
        print("similar")
    else:
        print("dissimilar")