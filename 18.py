input_number = input("Please enter a number: ")
dict = {}
try:
    input_number = int(input_number)
    for x in range(1,input_number+1):
        dict[x]=x*x
    print(dict, "is the required dictionary")
except ValueError:
        print("Please enter a valid number.")