ls = list(map(int, input().split()))
s = sum(ls)
x = s/5
x = x/20
if x > 4.0 and x <= 5.0:
    print('a')
elif x>3.0 and x<= 4.0:
    print('b')
elif x>2.0 and x<= 3.0:
    print('c')
else:
    print('f')