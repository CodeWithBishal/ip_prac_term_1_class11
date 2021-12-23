print("Press 1 to check if it's a BUZZ number")
print("Press 2 to check if it's a SPECIAL number")
print("Press 3 to find all the Prime Factors of the number")

choice = input("Please enter your choice: ")

if(choice == "1"):
    input_number = input("Please enter a number to check if it's a BUZZ number: ")
    try:
        input_number = int(input_number)
        if input_number%7 == 0 or input_number%10 == 7:
            print(input_number, "is a BUZZ number")
        else:
            print(input_number, "is not a BUZZ number")
    except ValueError:
        print("Please enter a valid number.")
elif(choice == "2"):
    input_number = input("Please enter a number to check if it's a SPECIAL number: ")
    try:
        input_number = int(input_number)
        first_digit = input_number // 10
        last_digit = input_number % 10
        sum = first_digit + last_digit
        multiply = first_digit * last_digit
        if (sum == multiply):
            print("The given number is a SPECIAL Number")
        else:
            print("The given number is not a SPECIAL number")
    except ValueError:
        print("Please enter a valid number.")
elif(choice == "3"):
    input_number = input("Please enter a number to find out the prime factors of the number: ")
    try:
        input_number = int(input_number)
        i = 2
        factors = []
        while i * i <= input_number:
            if input_number % i:
                i += 1
            else:
                input_number //= i
                factors.append(i)
        if input_number>1:
            factors.append(input_number)
        print(factors, "is the factor of the given number")
    except ValueError:
        print("Please enter a valid number.")