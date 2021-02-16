


def print_upper_words(words, must_start_with):
    """takes a list of words and letters and prints out the words in all caps if they begin with one of those letters"""

    

    for word in words:
        okay= False
        for letter in must_start_with:
            if word[0].upper()==letter.upper():
                okay = True
        if okay:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])
