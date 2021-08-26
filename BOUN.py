
k=int(input())
n=int(input())
ls = []
for p in range(n):
    ls.append(int(input()))
    
for i in ls:
    if k-i in ls and k-i!=i:
        print("true")
        break
else:
    print("false")
