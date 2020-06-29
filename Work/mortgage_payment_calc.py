# mortgage.py
#
# Exercise 1.7


years = 30 
total = 500000.0
interest = 0.05
payment = 2684.11
total_paid = 0.0
months = years * 12
month = 0

#1.9 Extra payments calc
start_additional = 61
end_additional = 108
additional_payments = 0
additional_payment_amount = 1000.00


while total > 0:
#    if additional_payments > 0:
#        total = total * (1 + interest/12) - (payment + additional_payment_amount)
#        additional_payments = additional_payments - 1
#        print (additional_payments, ' bonus payments left')
#
    if month >= start_additional and month <= end_additional:
        total = total * (1 + interest/12) - (payment + additional_payment_amount)
        total_paid = total_paid + (payment + additional_payment_amount)
    else:
        total = total * (1 + interest/12) - payment
        total_paid = total_paid + payment
    month = month + 1
    print(month, round(total_paid, 2), round(total, 2))
print('total is', round(total_paid, 2))

if total < payment:
    payment = total
    print(payment)