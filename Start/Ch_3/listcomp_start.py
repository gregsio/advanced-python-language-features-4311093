# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def square(arg1):
    return arg1**2

# TODO: Perform a mapping and filter function on a list
#square_evens=list(filter(lambda x: x<=16, map(square,evens)))
#square_evens=list(map(square,filter(lambda x: x < 10, evens)))

square_evens = [ e**2 for e in evens]
#print(square_evens)
# TODO: Derive a new list of numbers frm a given list

# TODO: Limit the items operated on with a predicate condition

square_odds = [o**2 for o in odds if o > 3 and o < 16]
print(square_odds)
