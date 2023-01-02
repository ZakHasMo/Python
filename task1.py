#This program needs to make use of for loops in order to display the times tables for any number.
n = int(input("Enter a number: "))

for x in range(1, 13):
    print(f"{n} * {x} = {n*x}")
    