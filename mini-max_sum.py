x=list(map(int(input("enter the list of element").split())))

#print(type(x))
min_list=[]
max_list=[]
for i in range(4):
    min_list.append(min(x))
    
    y=min(x)
    
    x.remove(y)
    
print(sum(min_list))

y=min_list
y.append(x[0])

for i in range(4):
    max_list.append(max(y))
    z=max(y)
    y.remove(z)
print(sum(max_list))
"""i creat a list of first 4 smallest elements by using min function and after appending each element
to min_list ,i removed that elemnt from input list
therby create an minlist and found sum
for finding max_list of 4 element i create y list basically which is minlist to which pending 1 element
of input list (that one elemnt which remains after removing elemet initially for min_list )is appended
there by doing same logic for creating
maxlist and find sum"""
    
    
