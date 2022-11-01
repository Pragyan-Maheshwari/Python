# Create a class for plant 
class plant:
    def __init__(self,Name,Height,Region):
        self.Name = Name
        self.Height = Height
        self.Region = Region
    def Giver(self):
        print({
            "Name" : self.Name,
            "Height" : self.Height,
            "Region": self.Region})

p = plant("Tulsi","75 cm","All")
p.Giver()