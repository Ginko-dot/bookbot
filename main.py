from stats import *
import sys

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    count = word_count(text)
    char_list = char_count(text)
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at", sys.argv[1])
    print ("----------- Word Count ----------")
    print ("Found", count ,"total words")
    print ("--------- Character Count -------")
    char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        print(f"{i['char']}: {i['num']}")
    print ("============= END ===============")
if __name__ == "__main__":
    main()