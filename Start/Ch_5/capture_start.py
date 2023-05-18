# Example file for Advanced Python: Language Features by Joe Marini
# Capture pattern matching for assigning values within the match

#name = input("What is your name? ")

class User():
    def __init__(self,*,fname,lname):
        self.fname = fname
        self.lname = lname

class Golfplayer(User):
    def __init__(self, *, fname, lname):
        self.player = 'Golf'
        super().__init__(fname=fname, lname=lname)

# match name:
#     case "":
#         print("Hello, anonymous!")
#     case "Grégory" | "Greg" | "Gregory":
#         print("oh, hey Greg! How's the Python training going?")
  
player1 = User(fname='Greg',lname='sar')
player2 = Golfplayer(fname='John', lname='Doe')

match player1:
    case User(fname=f, lname=l) if f == 'Greg':
        print(f"Welcome home Mister {player1.fname.capitalize()} {player1.lname.upper()}")
    case User():
        print(f"{player1.fname} {player1.lname.upper()} is a regular user")
    case _:
        print("Not a user")
