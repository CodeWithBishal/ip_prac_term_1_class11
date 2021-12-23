input_number = input("Please enter a series of number: ")



if (input_number == str(input_number)[::-1]):
    print("The given series of number is a palindrome.")
else:
    print("The given series of number is not a palindrome.")