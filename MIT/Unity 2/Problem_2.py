# program that calculates the minimum fixed amount to pay a loan within a period
balance = 3619
annualInterestRate = 20/100
months_to_pay = 12

fix_guess = 0
initial_balance = balance

while balance > 0:
    fix_guess += 0.01
    balance = initial_balance

    for month in range(months_to_pay):
        unpaid = balance - fix_guess
        balance = unpaid + (annualInterestRate/12) * unpaid

print("Lowest Payment: ${:.2f}".format(fix_guess))
