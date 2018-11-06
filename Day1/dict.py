#python program run as a module
#dictionary where the keys are numbers between 1 and 15 and the values are squares of the keys

d=dict()
for x in range(1,16):
    d[x]=x**2
    print(d)
