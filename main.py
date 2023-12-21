def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_char_list = convert_char_dict_to_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character appears {item['count']} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_char_dict_to_list(char_dict):
    chars = []
    for char in char_dict:
        chars.append({"char": char, "count": char_dict[char]})
    chars.sort(reverse=True, key=lambda item: item["count"])
    return chars

main()