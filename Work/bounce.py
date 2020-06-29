# bounce.py
#
# Exercise 1.5
height = 100
bounce_height = 3/5
bounce_num = 1

while bounce_num <= 10:
    height = height*bounce_height
    print(bounce_num, round(height))
    bounce_num = bounce_num + 1
