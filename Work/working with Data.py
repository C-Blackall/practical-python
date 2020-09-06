#working with Data

Data types

outside of Int, Float or String

None 
This is a place holder and defaults to false

Tuples
tuples ae immutable like strings so you can not change the contents

s = ('GOOG', 100, 49.1)
s = 'GOOG', 100, 49.1

special cas e Tuples
0 or 1 item

this is like a record in a database
a tuple is the line and you call the common


#tupels are similar to lists but tend to be mixed data for a single item rather then multiple items for a single result

#eg
record = ('GOOG', 100, 490.1)       # A tuple representing a record in a portfolio
symbols = [ 'GOOG', 'AAPL', 'IBM' ]  # A List representing three stock symbols

a dictionary is similar to a tuple but it is data assigned to the key

s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}


#with a dict you can reference the keys() or convert them to a list
'''
we can use del x['delete']
to remove an item in the dict

dicts are ab0out readability as much as anything else
'''


with a dictionary we can print the key

Containers
this is usually a list of Tuples
treat these as a list of records in a database

dict can be used as a Containers

#Formatting
f''
#example
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')


#Format codes (after the : inside the {}) are similar to C printf(). Common codes include:
'''
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
'''
#Common modifiers adjust the field width and decimal precision. This is a partial list:
'''
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
'''
