list = []
total = 0
input_number = input("Please enter a series of number: ") 

try: 
    input_number = int(input_number)
    for i in range(0, input_number+1):
        list.append(i)
    print(list, "is the required list of integer")
    for element in range(0, len(list)):
        total += list[element]
    average = total/element
    print(total, "is the total of all integer in the list")
    print(average, "is the average of all integer in the list")

except ValueError:
        print("Please enter a valid number.")