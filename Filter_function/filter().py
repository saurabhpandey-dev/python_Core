##The filter() function is used to select elements from an iterable that meet a
##specific condition.
##The filter() function accepts a function and an iterable for its arguments.


lst= ['rever','sky','tree','mountain']

def is_long_word(word):
    return len(word)>4

long_word = list(filter(is_long_word,lst))

print(long_word)
