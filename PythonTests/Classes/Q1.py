# Create class for polygon 

class Polygon:
    def __init__(self,poli):
        self.poli = poli
    def Get(self):
        input("Which Shape Had You Chosen? ")
        print(self.poli)

h = Polygon("Triangle")
h.Get()
        
