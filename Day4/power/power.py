def power(a, b):
#checking whether the two arguments are of data type in 
    if not ((isinstance(a, int) ) and isinstance(b, int)):
        return 'invalid input'

#if the base argument is 1 and of power zero return 1 by default
    if b == 0 or a == 1:
        return 1
#if the base agument is zero regardless of the power return 0
    if a == 0:
        return 0
#other wise if the base argument is greater or equal to one call the power function 
    if b >= 1:
        return a*power(a, b-1)

   
    return 1/(a*power(a, b-1))


if __name__ == '__main__':
    print(power(3, 4))
