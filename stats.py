def get_book_text (book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    length = len(text.split())
    return length
    
def char_count(text):
    text=text.lower()
    chars = {}
    for char in text:
        if char.isalpha():
            if char in chars:
                chars[char] +=1
            else:
                chars[char] =1

    char_list = []
    for char, count in chars.items():
            char_list.append({'char': char, 'num': count})
    return char_list

def sort_on(items):
    return items["num"]