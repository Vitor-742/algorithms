def is_anagram(first_string, second_string):
    string1 = list(first_string.lower())
    string2 = second_string.lower()
    try:
        for letter in string2:
            string1.remove(letter)
    except ValueError:
        return False
    if len(string1) == 0:
        return True
    else:
        return False
