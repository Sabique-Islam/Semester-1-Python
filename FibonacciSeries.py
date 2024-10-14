"""num = int(input("Enter the range:-"))
n1=0
n2=1
for i in range(num):
    print(n1)
    n1=n2
    n2=n1+n2"""

num = int(input("Enter the range:-"))

n1, n2 = 0, 1

for i in range(num):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2