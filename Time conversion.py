x=input("enter time in prescribed format:HH:MM:SSPM/AM")
newtime=""
#hh:mm:ssPM/AM
#0123456789
if x[8]=="A":
    if x[0]=="1" and x[1]=="2":
        newtime="00"
        for i in range(2,8):
            newtime=newtime+x[i]
    else:
         for i in range(1,8):
            newtime=newtime+x[i]
else:
    for i in range(1):
        if x[0]!=0:
            y=(int(x[0])*10+int(x[1]))+12
            newtime=newtime+str(y)
        else:
            newtime=newtime+str(int(x[1]+12))
    for i in range(2,8):
            newtime=newtime+x[i]
print(newtime)
        
