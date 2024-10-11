#WAP to check whether the number entered is positive, negative or 0.

num = input("Enter a number: ")

if num.lstrip('-').isdigit(): #lstrip() removes the '-' (if num is a negative integer) before isdigit() is called, because isdigit() only checks for non-negative integers.
    num = int(num)
    if num>0:
        print("The number entered is positive.")
    elif num<0:
        print("The number entered is negative.")
    elif num == 0:
        print("The number entered is 0.")
else:
    print("PLease enter a valid number...") 

# Issues: - 
# When input is a negative integer, else statement is executed along with it.
# Issue is fixed :)
