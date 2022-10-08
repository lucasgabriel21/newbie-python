# calculates the credit remaining value after a year paying the minimum amount
balance = 5000
annualInterestRate = 18/100
monthlyPaymentRate = 2/100

for month in range(1, 13):
    unpaid = balance - monthlyPaymentRate * balance
    balance = round(unpaid + annualInterestRate/12 * unpaid, 2)

print('Remaining balance: {}'.format(balance))
