str=input("Enter the string : ")

# casefold for converting into lower letter
str=str.casefold()  
if(str==str[::-1]):
    print("Yes, its is Palindrome ")
else :
    print("No, It is not Palindrome")
