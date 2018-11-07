def count_vowels(entry):
    if not isinstance(entry, str):
        return'invalid input'

    vowels = 'aeiou'
    new_vow = entry.lower()
    original_string = set(new_vow)
    duplicate = len(new_vow)-len(original_string)
    newstring = ""

    for i in vowels:
        if i in original_string:
            newstring += str(i)

    return (newstring, duplicate)


if __name__ == "__main__":

    print(count_vowels('ffggtree'))



