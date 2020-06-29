# mortgage.py
#
# Exercise 1.7


years = 30 
total = 500000.0
interest = 0.05
payment = 2684.11
total_paid = 0.0
months = years * 12

#1.8 Extra payments

additional_payments = 12
additional_payment_amount = 1000.00


while total > 0:
    if additional_payments > 0:
        total = total * (1 + interest/12) - (payment + additional_payment_amount)
        additional_payments = additional_payments - 1
        total_paid = total_paid + (payment + additional_payment_amount)
        print (additional_payments, ' bonus payments left')
    else:
        total = total * (1 + interest/12) - payment
        total_paid = total_paid + payment
print('total is', round(total_paid, 2))
