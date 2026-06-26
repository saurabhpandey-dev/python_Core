##Let's say you want to get the number of pages in book objects created with the
##class below, or compare them and get a readable string of the objects.
##Here's what happens without special methods:

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # TypeError: object of type 'Book' has no len()
print(str(book1)) # <__main__.Book object at 0x000001505B5996A0>
print(book1 == book2) # False even though they have the same number of pages


##len(book1) failed because Python doesn't know how to get the length of your
##book object without __len__()
##
##str(book1) printed something like <__main__.Book object at 0x000001505B5996A0>
##because that's the default representation when you don't use __str__()
##
##book1 == book2 resulted in False because Python just checks if both objects
##are the same in memory, not by content.
