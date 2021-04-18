n=int(input())
ls=[]
for _ in range(n):
  ls.append(int(input()))
ls.sort()
maxx=0
for i in range(n):
  price = ls[i]*(n-i)
  if price > maxx:
    maxx= price
print(maxx)