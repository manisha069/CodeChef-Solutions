t=int(input())
ls=[2010, 2015, 2016, 2017, 2019]
for _ in range(t):
    year=int(input())
    if year in ls:
        print("HOSTED")
    else:
        print("NOT HOSTED")