# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE
# length of the string
# the number of digit caraters
# the number of  caraters
# string with unique caracters
# size of the string

digits = [n for n in test_str if n.isnumeric()]
punct = [p for p in test_str if p in string.punctuation]
u_ltrs = "".join({
    l for l in test_str if l not in punct and not l.isnumeric()|l.isspace()})

# print the data
str_data = {
    'Length': len(test_str), 'Digits':len(digits) , 'Punctuations':len(punct),
    'Unique Letters': u_ltrs , 'Unique Count': len(u_ltrs)
}
pprint.pp(str_data)
