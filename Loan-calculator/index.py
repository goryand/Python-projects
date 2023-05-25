print("Hello python loan calculator!")

moneyOwed = float(input("How much money do you owe in dollars?"))
apr = float(input("What is the APR of the loan?"))
payment = float(input("How much will you pay off each month in dollars?"))
months = int(input("How many months do you want this loan?"))

# Determine monthly rate by converting APR into a decimal, and dividing by amount of months in a year
monthlyRate = apr / 100 / 12

for i in range(months):
    # Determine interest
    interestPaid = moneyOwed * monthlyRate

    # Calculate new final moneyOwed value
    moneyOwed = moneyOwed + interestPaid

    # Make virtual payment
    moneyOwed = moneyOwed - payment

    if moneyOwed - payment < 0:
        print("The final payment is ", moneyOwed)
        print("You paid off the loan in", i + 1, "months")
        break

    print("paid", payment, "of which", interestPaid, " was interest payment", "Now I owe", moneyOwed)
