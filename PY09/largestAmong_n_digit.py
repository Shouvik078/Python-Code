arr=[]
num=int(input("Enter N number : "))
for n in range(num):
    numbers=int(input("Enter number: "))
    arr.append(numbers)
print("Maximum element : ",max(arr))

print("Maximum element : ",min(arr))