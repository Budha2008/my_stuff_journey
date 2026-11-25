x=20
l=[]
for i in range(8):
    if x%2==0:
        l.append(0)
    else:
        l.append(1)
    x=x//2
    print(x)
print(l[::-1])    
