# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


def my_function(arg1, arg2=None):
    """
    my_function(arg1, arg2=None)
    Prints out the value of passed arguments arg1 and arg2
    Parameters:
        arg1: any value
        arg2: default to Node, can be any value as well
    """
    print(arg1, arg2)


print(my_function.__doc__)
