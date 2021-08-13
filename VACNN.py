t=int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ls=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
    if a in ls and b>=24:
        print("YES")
    else:
        print("NO")