# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgb_color':
            return (self.red,self.green,self.blue)
        elif attr == 'hexcolor':
            return f"#{self.red:x}{self.green:x}{self.blue:x}"
        else:
            raise AttributeError(f"Attribute {attr} is not valid")

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgb_color':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr,val)


    # TODO: use dir to list the available properties
    def __dir__(self):
        return ['rgb_color','hexcolor']

# create an instance of myColor
cls1 = MyColor()
# TODO: print the value of a computed attribute
print(cls1.rgb_color)
print(cls1.hexcolor)

# TODO: set the value of a computed attribute
cls1.rgb_color = (200, 125, 177)
print(cls1.rgb_color)
print(cls1.hexcolor)
# TODO: access a regular attribute

# TODO: list the available attributes
print(dir(MyColor()))
