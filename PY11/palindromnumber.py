n=int(input("Enter number : "))
temp=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("Palindrom Number ")
else:
    print("Not Palindrom Number ")
