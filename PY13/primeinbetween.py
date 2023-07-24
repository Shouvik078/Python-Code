def primes(a):
    for x in range(1,n+1):
        cn=x
        count=0
        for j in range(1,cn+1):
            if cn%j==0:
                count+=1
        if count==2:
            print(cn)

n=int(input("Enter a number : "))
print(primes(n))