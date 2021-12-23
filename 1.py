pi = 3.14159
query = input("Press 1 for finding the area \nPress 2 for finding the perimeter \n\n")
if type(query) == str:
    if (query == "1"):
        print("Please enter the radius of the circle in decimal:")
        radius = input()
        radius = float(radius)
        area = pi * (radius * radius)
        print("Area of the given circle is " + str(area))

    elif (query == "2"):
        print("Please enter the radius of the circle in decimal:")
        radius = input()
        radius = float(radius)
        perimeter = 2 * pi * radius 
        print("Perimeter of the given circle is " + str(perimeter))

    else:
        print("Please select a valid option and try again.")
else:
    print("Please select a valid option and try again.")