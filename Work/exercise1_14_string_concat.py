symb = 'AAPL,IBM,MSFT,YHOO,SCO'
symb = symb + ',GOOG'
symb = 'HPQ,' + symb 
symb

#1.15
'''
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
'''
#AA is true as it string matches AAPL

#1.16
'''
>>> symb.lower()
'hpq,aapl,ibm,msft,yhoo,sco,goog'
>>> symb
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>> lowersymb = symb.lower()
>>> lowersymb
'hpq,aapl,ibm,msft,yhoo,sco,goog'
'''

#test others
'''
>>> symb.find('MSFT')
13
>>> symb[13:17]
'MSFT'
>>> symb = symb.replace('SCO','DOA')
>>> symb
'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
>>> name = '    IBM     \n'
>>> name
'\tIBM\t\n'
>>> name = name.strip()
>>> name
'IBM'
'''

#1.17:  f-strings
'''
>>> shares = 100
>>> price = 91.1
>>> f'{shares} sharesof {name} at ${price:0.2f}'
'100 sharesof IBM at $91.10'
'''
