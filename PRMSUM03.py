def isprime(n):
    if n %2 ==0:
        return False
    else:
        for i in range(3, n, 2):
            if n%i==0:
                return False
        else:
            return True
            


def prime(n):
    ls=[]
    if n ==1:
        print(1)
    if n==2:
        print(2)
    else:
        ls.append(2)
        i=3
        while len(ls)<n:
            if isprime(i):
                ls.append(i)
            i+=1
    print(sum(ls))

n=int(input())
prime(n)