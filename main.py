from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    temp = count_chars(book_text)
    print(temp)
    
    
main()