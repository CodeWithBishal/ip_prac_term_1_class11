input_number = input("Please enter a series of number: ")
sum_of_digits = 0

try:
    for digits in str(input_number):
        sum_of_digits += int(digits)
    print(sum_of_digits)
except ValueError:
    print("Please enter a valid number.")