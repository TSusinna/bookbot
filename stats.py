def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def get_num_words(filepath):
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        return len(words)

def each_character_times(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.lower()
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    
def sort_dictionary(dictionary):
    dictionaries = []
    for key, value in dictionary.items():
        dictionaries.append({"character": key, "count": value})
    dictionaries = sorted(dictionaries, key=lambda x: x["count"], reverse=True)
    return dictionaries

def print_report(filepath):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words\n--------- Character Count -------")
    for dict in sort_dictionary(each_character_times(filepath)):
        if dict["character"].isalpha() == True:
            print(f"{dict['character']}: {dict['count']}")
    print("============= END ===============")