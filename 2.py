character = input("Please enter any character: ")

if character.isupper():
    print("The given value is a Uppercase character")
elif character.islower():
    print("The given value is a lowercase character")
elif character.isnumeric():
    print("The given value is a Numeric character")
elif type(character) == str:
    print("The given value is a String")