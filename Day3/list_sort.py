def list_sort(lista):

    even = []
    odd = []
    characters = []
    new_list = dict()
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        new_list['evens'] = even
        new_list['odds'] = odd
        new_list['chars'] = characters
        return new_list

    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)

    new_list['evens'] = sorted(even)
    new_list['odds'] = sorted(odd)
    new_list['chars'] = sorted(characters)
    return new_list


print(list_sort([0,8,1, 7, 9,5,3,'p', 'b','m']))
