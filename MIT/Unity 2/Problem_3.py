# bisection search of the minimum fixed amount (monthly) to pay a loan within a year
balance = 999999
annualInterestRate = 0.18

lower = balance / 12  # as if there was no interest
upper = (balance * (1 + annualInterestRate/12)**12) / 12  # as if there was no amortization
fixed_payment = (lower + upper) / 2  # bisection
initial_balance = balance

while abs(balance) >= 0.01:
    balance = initial_balance

    for month in range(12):
        unpaid = balance - fixed_payment
        balance = unpaid + (annualInterestRate / 12) * unpaid

    if balance > 0:
        lower = fixed_payment
    else:
        upper = fixed_payment

    fixed_payment = (lower + upper) / 2

print("Lowest Payment: {:.2f}".format(fixed_payment))
