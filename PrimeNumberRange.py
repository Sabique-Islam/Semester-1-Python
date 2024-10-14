"""a = int(input("Enter the lower range: "))
b = int(input("Enter the upper range: ")) 
isPrime=True
for num in range(a,b+1):
        for i in range(2, int(num/2)):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:   
         print(num, end=" ")"""

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    if num < 2:
        continue
    
    is_prime = True
    for i in range(2, int(num**0.5) + 1): #least time complexity
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")