lst= ['rever','sky','tree','mountain']

def is_long_word(word):
    return len(word)>4

long_word = list(filter(is_long_word,lst))

print(long_word)
