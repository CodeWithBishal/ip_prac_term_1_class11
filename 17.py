list = eval(input("Enter a list: "))
max_list = max(list)
min_list = min(list)
print("The maximum value in the list is " + str(max_list) + " at index " + str(list.index(max_list)))
print("The minimum value in the list is " + str(min_list) + " at index " + str(list.index(min_list)))