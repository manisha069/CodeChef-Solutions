t = int(input())
even=0
 
ls=list(map(int, input().split()))
for i in ls:
    if i %2==0:
        even=even+1
if even> (t-even):
    print("READY FOR BATTLE")
else:
    print("NOT READY")