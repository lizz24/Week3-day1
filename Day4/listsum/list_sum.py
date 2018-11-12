def list_sum(lista):
#validating the argument that it should be of list tpye
    if not isinstance(lista, list):
        print('Invalid input')
    
#Iterating through the list by calling the function recursively    
    listadd = 0
    for n in lista:
        if  isinstance(n, list):
           
            listadd+=list_sum(n)
        else:
             listadd+= n

    return listadd

if __name__ == '__main__':
 print(list_sum([ 1, 2, [3, 4]]))
