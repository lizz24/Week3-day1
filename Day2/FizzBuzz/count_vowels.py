def count_vowels(entry):
#checking if the input variable is of datatype string    
    if not isinstance(entry, str):
        return'invalid input'
#initializing vowels to a string
    vowels = 'aeiou'
#making sure that the input string are lowercase    
    new_vow = entry.lower()
    original_string = set(new_vow)
#evaluating the length of duplicates in the string    
    duplicate = len(new_vow)-len(original_string)
    newstring = ""
#iterating through the string checking for only duplicate vowels
    for i in vowels:
        if i in original_string:
            newstring += str(i)

    return (newstring, duplicate)


if __name__ == "__main__":
# sample data for input string 
    print(count_vowels('ffggtree'))



