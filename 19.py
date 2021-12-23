keys = {'A':1, 'B':2, 'C':3, 'D':4}
input_key = input("Enter a key: ")

if input_key in keys.keys():
    print(keys[input_key], "is the value of the Key " + input_key)
else:
    print("Key does not exist in the dictionary")
