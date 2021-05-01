# cook your dish here
n=int(input())
aa=[]
bb=[]
for i in range(n):
    a,b=map(int, input().split())
    aa.append(a)
    bb.append(b)

suma=0
sumb=0
ans=list()
for i in range(n):
    suma=suma+aa[i]
    sumb=sumb+bb[i]
    if suma>sumb:
        ans.append(["1", suma-sumb])
    else:
        ans.append(["2", sumb-suma])

max=0
index=0
for i in range(len(ans)):
    if(ans[i][1]>max):
        max=ans[i][1]
        index=i;
print(ans[index][0], ans[index][1])