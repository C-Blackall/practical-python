#function
def sumabc(n):
    '''
    sum of n 
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumabc(10)

'''
 use the raise statement to exit  a function
 '''
 