def print_upper_words(words, must_start_with):
    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})