#1.6 Filemanagment
'''
f = open('foo.txt', 'rt')
g = open('bar.txt', 'wt')
data = f.read()
g.write('some text')
f.close()
g.close()

with open('foo.txt', rt) as file:
    #do something
    file.write('a')

with open ('outfile', 'wt') as out:
    out.write('Hellow World\n')
with open ('outfile', 'wt') as out:
    print('Hello World', file=out)
'''


import os
