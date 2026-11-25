n=int(input("enter the number of rows and colum which will be same"))
ls=eval(input("enter the stuff in prescribed format"))
l=[]
for i in  ls:
   
    sorted_string = ''.join(sorted(i))#this line of code i take from geeksforgeeks
    #print(sorted_string)
    l.append(sorted_string)
#print(l)
l2=[]
for i in range(n):
    string=""
    for j in range(n):
       string=string+l[j][i]
    l2.append(string)
#print(l2)
flag=1
for i in range(n):
    for j in range(n-1):
        if ord(l2[i][j])>ord(l2[i][j+1]):
            print("NO")
            flag=0
            break
if flag==1:
    print("yes")
        
        
        
