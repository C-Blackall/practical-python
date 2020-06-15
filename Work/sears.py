#sears.py

billthick = 0.11 *0.001
building_height = 442
bills = 1
day = 1

while bills * billthick < building_height:
    print(day, bills, bills * billthick)
    bills = bills * 2
    day = day + 1

print('Number of Days is', day)
print('Number of Bills', bills)