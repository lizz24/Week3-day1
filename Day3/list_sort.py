def list_sort(lista):
#Intializing three list variables
    even = []
    odd = []
    characters = []
#The new created list should return a dictionary    
    new_list = dict()
#checking the validity of the input variable whether it is a list    
    if not isinstance(lista, list):
        return 'Invalid Input'
#The input list should be equal to resultant(new_list) list with even, oddnumbers and character strings
    if not lista:
        new_list['evens'] = even
        new_list['odds'] = odd
        new_list['chars'] = characters
        return new_list
#iterating through the list checking for even, odd numbers and character strings
    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)
# sorting the list
    new_list['evens'] = sorted(even)
    new_list['odds'] = sorted(odd)
    new_list['chars'] = sorted(characters)
    return new_list

#sample data for input variable list 
print(list_sort([0,8,1, 7, 9,5,3,'p', 'b','m']))
