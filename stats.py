import sys

# def get_num_words(): 
#     with open("/home/acharyaylor/bookbot/books/frankenstein.txt") as f:
#         file_contents = f.read()
#         word_count = file_contents.split()
#         count = 0
#         for i in word_count:
#             count += 1
#         print(f" Found {count} total words")

def get_num_words(): 
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        word_count = file_contents.split()
        count = 0
        for i in word_count:
            count += 1

        print(f" Found {count} total words")

def get_num_chars(): 
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        char_dict = {}
        for i in file_contents:
            if i.lower() in char_dict:
                char_dict[i.lower()] += 1
            else:
                char_dict[i.lower()] = 1
        return char_dict
    
def char_report():
    char_dict = get_num_chars()
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    # for char, count in sorted_chars:
    #     if char == "\n":
    #         char = "newline"
    #     elif char == " ":
    #         char = "space"
    #     print(f"'{char}': {count}")
    return sorted_chars

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:          
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    get_num_words()
    print("--------- Character Count -------")
    sorted_chars2 = char_report()
    for char, count in sorted_chars2:
        if char == "\n":
            char = "newline"
        elif char == " ":
            char = "space"
        print(f"{char}: {count}")
    print("============= END ===============")
