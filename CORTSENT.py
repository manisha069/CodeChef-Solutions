l1 ="abcdefghijklm"
l2="NOPQRSTUVWXYZ"
t=int(input())
for _ in range(t):
    ls=list(input().split())
    k = int(ls[0])
    ls=ls[1:]
#     print("ls", ls)
    count=0
    for i in ls:
#         print("i ", i)
        if i.islower():
#             print("lower", i.islower())
            if set(i).issubset(set(l1)):
#                 print("set i", set(i))
                count+=1
        elif i.isupper():
#             print("upper", i.isupper())
            if set(i).issubset(set(l2)):
#                 print("set i", set(i))
                count+=1

    if count==k:
        print("YES")
    else:
        print("NO")