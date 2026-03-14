number = input("Enter a number: ").split()

if (number[0:] == number[::-1]):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
copy_number = number.copy()
copy_number.reverse()

if (number == copy_number):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")    