#python program run as a module
#dictionary where the keys are numbers between 1 and 15 and the values are squares of the keys


#Assigning variable d to a dictionary data type
d=dict()
# getting the range of the dictionary from 1 - 16
for x in range(1,16):
#squaring each number in range
    d[x]=x**2
    print(d)
