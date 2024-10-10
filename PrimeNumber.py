# WAP to check whether the entered number is prime or not.
"""
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")

else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break

    else:
        print(f"{num} is a prime number.") 
"""

# To avoid errors when the input in some string:-

num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    
    if num <= 1:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(num/2)): #typecasting is done because int/int = float output
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
else:
    print("Enter a number...")
