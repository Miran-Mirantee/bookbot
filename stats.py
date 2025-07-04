def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(string: str) -> int:
    arr = string.split()
    return len(arr)

def count_chars(string: str) -> dict[str, int]:
    chars_dict = dict()
    words = string.lower().split()
    for word in words:
        for char in word:
            if char in chars_dict:
                chars_dict[char] = chars_dict.get(char) + 1
            else:
                chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items[1]

def report_chars(filepath: str):
    book_text = get_book_text(filepath)
    chars_list = list(count_chars(book_text).items())
    sorted_chars_list = sorted(chars_list, key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    
    for chars in sorted_chars_list:
        print(f"{chars[0]}: {chars[1]}")
    
    print("============= END ===============")