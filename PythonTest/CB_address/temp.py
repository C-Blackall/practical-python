#this file will  be migrated into the main.py
import logging

(name, address, number)
storedAddress = (a, 'b', 1)

newBook = {}

def newContact():
    new = (c, 'd', 2)
    address = storedAddress + new
    print address
    logging.info('added new address')


def search(contact, address):
    if contact in address:
        print contact
    else
        logging.info('contact does not exist')
        #would user want to add contact
        if add is true:
            newContact(name = contact)


a = ('a', 'b', 1)
b= ('a','1 a st', 3)
a
c = (a , 'asdd', 3456)

book = {}
book = {1:a,2:b}
print(book)

book = book.append(c)

'''
>>> a = {'tuple': (23, 32)}
>>> a
{'tuple': (23, 32)}
>>> a['tuple'] = (42, 24)
>>> a
{'tuple': (42, 24)}
>>> del a['tuple']
>>> a
{}
'''

#######

import csv

d = {}
with open /home/users/callumb/local_git/practical-python/Python Test/CB_address/Data/Sample.csv as f:
    for key in csv.reader(f):
        d[key] = tuple(map(name, address, number))
print (d)
