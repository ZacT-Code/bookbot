def get_num_words(): 
    with open("/home/acharyaylor/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        count = 0
        for i in word_count:
            count += 1

        print(f" Found {count} total words")

def get_num_chars(): 
    with open("/home/acharyaylor/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        char_dict = {}
        for i in file_contents:
            if i.lower() in char_dict:
                char_dict[i.lower()] += 1
            else:
                char_dict[i.lower()] = 1
        return char_dict