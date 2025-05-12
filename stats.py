# Opnens a file and returns the text in it
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

# Opens a file, reads its text and returns the number of words in it
def get_num_words(filepath):
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        return len(words)

# Counts the number of times each character appears in the text and returns a dictionary with the character as the key and the number of times it appears as the value
def each_character_times(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.lower()
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

# Sorts the dictionary by the number of times each character appears in the text and returns a list of dictionaries with the character and the number of times it appears
def sort_dictionary(dictionary):
    dictionaries = []
    for key, value in dictionary.items():
        dictionaries.append({"character": key, "count": value})
    dictionaries = sorted(dictionaries, key=lambda x: x["count"], reverse=True)
    return dictionaries

# Prints a report of the number of words in the text and the number of times each character appears in the text
def print_report(filepath):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words\n--------- Character Count -------")
    for dict in sort_dictionary(each_character_times(filepath)):
        if dict["character"].isalpha() == True:
            print(f"{dict['character']}: {dict['count']}")
    print("============= END ===============")