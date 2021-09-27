t=int(input())
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for _ in range(t):
    
    s=input()
    v=0
    for i in s:
        if i in vow:
            v+=1
    print(v, len(s)-v)  