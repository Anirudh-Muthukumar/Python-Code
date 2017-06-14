balance=3329
monthlyPaymentRate=0.02
annualInterestRate=.2
payment=0.0
remaining=0.0
paid=0.0

for i in range(0,12):
    payment=balance*monthlyPaymentRate
    remaining=balance-payment+(annualInterestRate/12.0*(balance-payment))
    balance=remaining
    paid+=payment
    print 'Month: '+str(i+1)
    print 'Minimum monthly payment: '+str(round(payment,2))
    print 'Remaining balance: '+str(round(balance,2))

print 'Total paid: '+str(round(paid,2))
print 'Remaining balance: '+str(round(balance,2))
    