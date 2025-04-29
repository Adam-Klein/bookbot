def count_words(book_text):
    the_book = book_text.split()
    num_words = 0
    for word in the_book:
        num_words += 1
    return num_words

def char_count(book_text):
    counts = {}
    for char in book_text:
        lchar = char.lower()
        if lchar not in counts:
            counts[lchar] = 0
        counts[lchar] += 1
    return counts

def sorted_list(counts):
    sorted_counts = {}
    for char in counts:
        if char.isalpha():
            sorted_counts[char] = counts[char]
    return sorted(sorted_counts.items(),reverse=True, key=lambda item: item[1])