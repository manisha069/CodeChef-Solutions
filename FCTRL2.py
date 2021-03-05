def facto(x):
    if x==1:
        return 1
    else:
        return x* facto(x-1)

n=int(input())
s=[]
for _ in range(n):
    s.append(int(input()))
    
for i in range(len(s)):
    print(facto(s[i]))
    