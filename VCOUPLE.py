t=int(input())
for _ in range(t):
    n=int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    boys.sort()
    girls.sort()
    girls.reverse()
    maxx= girls[0]+ boys[0]
    for i in range(1, n):
      if boys[i]+girls[i]>maxx:
        maxx=boys[i]+girls[i]
    print(maxx)