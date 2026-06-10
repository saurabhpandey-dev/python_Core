##str.maketrans(): This method is used to create a table of 1 to 1 character
##mappings for translation. It is often used with the translate() method which
##applies that table to a string and return the translated result.


trans_table = str.maketrans('abc', '123')
print(trans_table) # {97: 49, 98: 50, 99: 51}

result = 'abcabc'.translate(trans_table)
print(result)  # 123123
