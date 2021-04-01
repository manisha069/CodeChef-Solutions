x, y = input().split()              
x = float(x)                        
y = float(y)    
if (x+0.5 > y or x%5 != 0):
    pass
else:
    y = y-(x+0.5)
print(y)