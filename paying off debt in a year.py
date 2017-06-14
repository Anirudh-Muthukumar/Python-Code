balance=3329
annualInterestRate=0.2
monthlyInterestRate=annualInterestRate/12.0
payment=00.0
while balance:
    for i in range(12):
        payment=balance*monthlyInterestRate;
        balance=balance-payment+((annualInterestRate/12.0)*(balance-payment))
    payment+=10.0
    print balance
    
print round(payment,2)