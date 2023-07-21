import math

a=int(input("Enter a Value : "))
for x in range(2,int(a/2)+1):
    if(a%x)==0 :
        print(a," is not Prime")
        break
else:
    print(a," is prime number ")

