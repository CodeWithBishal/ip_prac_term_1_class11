total = input("Please enter the total cost of the item/items bought: ")
try: # using try-except to validate the input value 
    total = float(total)
    if total <= 2000:
        discount = (5/100)*total
        final_price = total - discount
        print("Final price after discount is " + str(final_price))

    elif 2000 < total <= 5000:
        discount = (25/100)*total
        final_price = total - discount
        print("Final price after discount is " + str(final_price))

    elif 5000 < total <= 10000:
        discount = (35/100)*total
        final_price = total - discount
        print("Final price after discount is " + str(final_price))

    elif total > 10000:
        discount = (50/100)*total
        final_price = total - discount
        print("Final price after discount is " + str(final_price))
except ValueError:
    print("Invalid data please try again.")