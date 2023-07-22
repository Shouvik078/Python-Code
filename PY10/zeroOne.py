n=int(input("Enter a Value : "))
for x in range(1,n+1):
    for y in range(1,n+1):
        print( (x+y)%2,end=" ")
    print()
