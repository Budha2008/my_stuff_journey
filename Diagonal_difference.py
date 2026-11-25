row=int(input("enter the number of row"))
m=[]
sum_diagonal1=0
sum_diagonal2=0
for i in range(row):
    element=list(map(int,input("enter the element in rows").split()))
    m.append(element)
    print(element)
for i in range(row):    
 sum_diagonal1= sum_diagonal1+m[i][i]
 sum_diagonal2=sum_diagonal2+m[i][(row-1)-i]
print(sum_diagonal1,sum_diagonal2)
if sum_diagonal1>sum_diagonal2:
    print(sum_diagonal1-sum_diagonal2)

elif sum_diagonal1<sum_diagonal2:
    print(sum_diagonal2-sum_diagonal1)
else:
    print(0)
