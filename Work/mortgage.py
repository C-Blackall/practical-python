# mortgage.py
#
# Exercise 1.7


years = 30 
total = 500000.0
interest = 0.05
payment = 2684.11
total_paid = 0.0

while total > 0:
    total = total * (1 + interest/12) - payment
    total_paid = total_paid + payment
#print('total is', round(total_paid, 2))
print(f'The total ammount that has been paid ${total_paid:0.2f}')