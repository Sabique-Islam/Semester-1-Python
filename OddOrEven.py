# WAP to check whether the number entered is even or odd.

"""
num = input("Enter a number: ")

if int(num)%2 == 0:
    print(f"{num} is an even number.")
elif int(num)%2 != 0:
    print(f"{num} is an odd number.")   

"""
    
# A better version for the above code:-
# Includes usage of function and try-except block.

def oddoreven():
    while True:
        user_input = input("Enter a number (or 'n' to exit): ")

        if user_input.lower() == 'n':
            print("Program terminated.")
            break

        try:
            num = int(user_input) #typecasting
            if num % 2 == 0:
                print(f"{num} is an even number.")
            else:
                print(f"{num} is an odd number.")
        except ValueError:
            print("Please enter a number...")

oddoreven()
