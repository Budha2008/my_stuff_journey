n=int(input("enter the number of otems"))
ls=list(map(int,input("enter it").split()))
counts=[]
for i in range(n):
    count=0
    for j in range(n):
        
        if i==ls[j]:
            count=count+1
    counts.append(count)
    count=0
print(counts)
