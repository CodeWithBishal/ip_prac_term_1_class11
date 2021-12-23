print("Press 1 for printing the series upto n terms")
print("Press 2 for printing the sum of the given series S = 1/2 + 3/4 + 5/6 + 7/8 + . . . . + 19/20")

choice = input("Please enter your choice: ")

if(choice == "1"):
    input_number = input("Please enter a number: ")
    try:
        for i in range(1, (int(input_number)+1)):
            i = i * i -1
            print(i)
    except ValueError:
        print("Please enter a valid number.")
elif(choice == "2"):
    sum = 0
    for i in range(2, 22, 2):
        sum += 1 - (1/i)
    print(sum, "is the sum of given series")
else:
    print("Out of Range")