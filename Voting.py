# WAP to check whether a person is eligible for voting.

"""
age = int(input("Enter age of the person: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")   """

# To avoid ValueError:-

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    
    if age >=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("Please enter your age in numeric form..")            
