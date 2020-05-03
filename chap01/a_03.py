import re
from string import ascii_lowercase

def split_words(str):
    list_of_words = list(map(lambda x: re.sub(r"\W+", "", x), str.split(" ")))
    number_of_character = list(map(len, list_of_words))
    return list_of_words, number_of_character
        

print(split_words("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
