#1.5 lists.py
names = ['Elwood', 'Jake', 'Smith']
nums = [39, 38, 42, 24, 65, 111]

print(names)
names.append('Murphy')
names.insert(2,'Aretha')
print(names)

s = [1,2,3]
t = ['a', 'b']
print(s + t)


#sorting
print(nums)
nums.sort()
print(nums)

#list math
numm = nums
x = numm * 2
print(x)
xv = numm + [34,25,4]
print(xv)

#symb
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
print(symbols)
sylist = symbols.split(',')
print(sylist)

#1.19

print(sylist[0])
print(sylist[1])
print(sylist[1])
print(sylist[-2])

print(sylist)
sylist[2] = 'AIG'
print(sylist)

mysyms = []
mysyms.append('GOOG')
print(mysyms)

sylist[-2:] = mysyms
print(sylist)

#1.20

for s in sylist:
    print('s =', s)

#1.21 mebership tests
if 'AIG' in sylist:
    print('a')
if 'BSB' in sylist:
    print('b')
print('c')

#1.22
sylist.append('RHT')
sylist.insert(2,'AA')
sylist.remove('MSFT')
sylist.append('YHOO')
print(sylist)

y = sylist.index('YHOO')
print(y)
print(sylist[y])
n = sylist.count('YHOO')
print(n)
p = sylist.remove('YHOO')
print(p)
print(sylist)
print('list is ',sylist)
#1.23
srt = list(sylist)
srt.sort()
print(srt)
print('list is ',srt)

srt.sort(reverse=True)
print(srt)


#1.24
a = ','.join(sylist)
print(a)
b = ':'.join(sylist)
print(b)
c = ''.join(sylist)
print(c)

#1.25
nums = [101, 102, 103]
items = ['spam', sylist, nums]
print(items)
print(items[0])
print(items[0][0])
print(items[1][1])
print(items[2][2])