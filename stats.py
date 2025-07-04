def count_words(string):
    arr = string.split()
    return len(arr)

def count_chars(string):
    chars_dict = dict()
    words = string.lower().split()
    for word in words:
        for char in word:
            if char in chars_dict:
                chars_dict[char] = chars_dict.get(char) + 1
            else:
                chars_dict[char] = 1
    return chars_dict