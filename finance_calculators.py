import math
calculator = input("Chose either 'investment or 'bond' from the menu below to proceed:\n investment - to calculate the amiunt of interest you'll earn on your savings\n bond - to calculate the amount you'll have to pay to a home loan\n Enter your preferred program: ")
if calculator.lower() == "investment":
    money = float(input("How much money are you depositing?: "))
    rate1 = float(input("What is the interest rate (as a percentage)?: "))
    num_years = float(input("How many years do you plan on investing?: "))
    interest = input("Do you want a 'simple' or 'compound' interest?: ")
    if interest.lower() == "simple":
        r1 = rate1/100
        simple_interest = float(money) * (1 + r1 * float(num_years))
        print("The total amount is " + str(round(simple_interest, 2)))
    elif interest.lower() == 'compound':
        r1 = rate1/100
        compound_interest = float(money) * math.pow((1 + float(r1)),num_years )
        print("The total amount is " + str(round(compound_interest, 2)))

elif calculator.lower() == 'bond':
    val_house = float(input("What is the value of the house?: "))
    rate2 = float(input("What is the annual interest rate?: "))
    months = float(input("How many months do you plan to take to repay the bond?: "))
    r2 = rate2/100/12
    bond = (float(r2) * float(val_house)) / (1 - (1 + float(r2)) ** (-abs(months)))
    print("The amount you'll have to be repaid on a home loan each month is " + str(round(bond, 2)))







