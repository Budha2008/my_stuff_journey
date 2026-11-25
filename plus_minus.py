n=int(input("size of array"))
array=[]
count_P=0
count_N=0
count_0=0
for i in range(n):
    
    x=int(input("the element"))
    array.append(x)
#print(array)
for i in array:
    if i>0:
        count_P=count_P+1
    elif i<0:
        count_N=count_N+1
    else:
        count_0=count_0+1
print(round(count_P/n,6),round(count_N/n,6),round(count_0/n,6),sep="\n")


#problem:i an not geting 6 decimal at some point when all decimals are zero
#idk:how to take all elemnt at an time without using eval
        
    
