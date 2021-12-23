input_number = input("Please enter a series of number: ")
sum_of_digits = 0

try:
    for digits in str(input_number):
        for number in str(digits):
            if int(number) % 2 != 0:
                sum_of_digits += int(number)
    print(sum_of_digits, "is the sum of all odd digits in the given series")
except ValueError:
    print("Please enter a valid number.")