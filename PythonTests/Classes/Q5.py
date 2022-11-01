# Create a class for phone

class Phone():
    def __init__(self,Name,Company,Color):
        self.Name = Name
        self.Color =Color
        self.Company =Company
    def Giver(self):
        print({
            "Name" : self.Name,
            "Complany" : self.Company,
            "Color":self.Color})

u = Phone("IPhone 40","Apple","Red")
u.Giver()