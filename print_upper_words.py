def print_upper_words (words) :
    up = input("enter first letter to make uppercase word: ")
    up.lower()
    for word in words :
        if words[words.index(word)][0] == up or words[words.index(word)][0] == up.upper() :
            print(words[words.index(word)].upper())
                   




