n = int(input("Enter a number: "))
for i in range(n):
    i+=1
    print("\n")
    for k in range(n-i):
        k-=1
        print(" ", end=" ")
    for j in range(i):
        j+=1
        print("*", end=" ")
    for l in range(i):
        print("*", end=" ")


# CLASS CODE

"""rows = 5
for i in range(1,rows+1):
    for j in range(rows-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()   """
