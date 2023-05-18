# Example file for Advanced Python: Language Features by Joe Marini
# demonstrate template string functions
from string import Template

# Usual string formatting with f-strings
str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = Template("You're watching ${a} by ${b}")

#s = Template('$who likes $what')

my_dict = {
    'a': str1,
    'b': str2
}
print(outputstr.substitute(my_dict))


# TODO: create a template with placeholders
message = Template('Please say "Hi!" to ${to} from ${from}')
# TODO: use the substitute method with keyword arguments
meassage_dict = {
    'from': 'Greg',
    'to': 'Chloe'
}
print(message.substitute(meassage_dict))
# TODO: use the substitute method with a dictionary
