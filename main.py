from stats import get_book_text, char_count, word_count, sorting
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    result = char_count(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(sys.argv[1])} total words")
    print("--------- Character Count -------")
    sorting(result)
    print("============= END ===============")

main()