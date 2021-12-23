input_number = input("Please enter a number: ")
sum = 0
try:
    input_number = int(input_number) 
    total = input_number
    while total > 0:
        digits = total % 10
        sum += digits ** 3
        total = total // 10
    if input_number == sum:
        print("This is an Armstrong Number")
    else:
        print("This is not an Armstrong Number")
except ValueError:
    print("Please enter a valid number.")