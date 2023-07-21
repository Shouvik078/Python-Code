def fact(n):
    if n<=1:
        return n
    else :
        n=n*fact(n-1)
        return n
    
a=int(input("Enter a Number : "))
print("Factorial of", a,"is :",fact(a))