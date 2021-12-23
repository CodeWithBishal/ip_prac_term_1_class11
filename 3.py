employee_name = input("Please enter Employee Name: ")

basic_pay = input("Please enter basic pay of the employee: ")

try: # using try-except to validate the input value 
    basic_pay = float(basic_pay)
    employee_name = str(employee_name)
    dearness_allowance = (25/100)*basic_pay
    house_rent = (15/100)*basic_pay
    provident_fund = (8.33/100)*basic_pay
    net_pay = basic_pay + dearness_allowance + house_rent
    gross_pay = net_pay - provident_fund

    print("Gross pay of the employee " + employee_name + " with basic pay of " + str(basic_pay) + " is " + str(gross_pay))
    
except ValueError:
    print("Invalid data please try again.")