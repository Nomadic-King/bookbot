def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print("\n--- Letter Counts ---")
    for letter, count in sorted(num_letters.items(), key=lambda x: (-x[1], x[0])):
        print(f"Letter '{letter}' was found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    num_letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in num_letters:  
                num_letters[letter] += 1
            else:
                num_letters[letter] = 1
    return num_letters

if __name__ == "__main__":
    main()