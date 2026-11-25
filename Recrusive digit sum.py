x=int(input("enter the digit"))
def superdigit(n):
    if n<=9:
        print("superdigit is",n)
    else:
        sum=0
        while n>0:
            sum=sum+n%10
            n=n//10
        if sum<=9:
            print("superdigit is",sum)
        else:
            superdigit(sum)
superdigit(x)
