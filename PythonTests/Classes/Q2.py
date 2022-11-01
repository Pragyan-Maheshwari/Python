# Create a class for bird
class Bird:
    def __init__(self,Name,Height):
        self.Name = Name
        self.Height = Height
    def Giver(self):
        print({
            "Name" : self.Name,
            "Height":self.Height})

j = Bird("Ostrich","10 feet")
j.Giver()