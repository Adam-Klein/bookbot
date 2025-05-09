from stats import count_words
from stats import char_count, sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    print(f"{num_words} words found in the document")
    letter_counts = char_count(book)
    print(letter_counts)
    sorted_counts = sorted_list(letter_counts)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in sorted_counts:
        print(f"{char[0]}: {char[1]}")
#        print(f"{char}: {sorted_counts[char]}")
    print(f"============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()