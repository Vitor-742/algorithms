def is_palindrome_recursive(word, low_index, high_index):
    if (not word):
        return False
    # caso o a palavra tenho chego ao final
    if high_index - low_index < 1:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
