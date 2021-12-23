# First Part

english_marks = input("Please enter your English marks: ")

physics_marks = input("Please enter your Physics marks: ")

chemistry_marks = input("Please enter your Chemistry marks: ")

maths_marks = input("Please enter your Maths marks: ")

ip_marks = input("Please enter your IP marks: ")

try:
    english_marks = float(english_marks)
    physics_marks = float(physics_marks)
    chemistry_marks = float(chemistry_marks)
    maths_marks = float(maths_marks)
    ip_marks = float(ip_marks)

    total_marks = english_marks + physics_marks + chemistry_marks + maths_marks + ip_marks
    round_marks = int(round(total_marks))
    print("You got " + str(round_marks) + " marks in total.")

    average_marks = (total_marks/5)
    print("Your average mark is " + str(average_marks))

    # Second Part

    if(average_marks >= 85):
        print("You got A grade.")

    elif(average_marks >= 70):
        print("You got B grade.")

    elif(average_marks >= 50):
        print("You got C grade.")

    elif(average_marks >= 40):
        print("You got D grade.")
    else:
        print("Failed!!")

except ValueError:
    print("Invalid data please try again.")

