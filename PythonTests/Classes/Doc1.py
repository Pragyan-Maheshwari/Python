class car:
    def __init__(self,nme,color,seats,feature1,feature2,feature3):
        self.nme = nme
        self.color = color
        self.seats = seats
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3
    def details(self):
        print({
            "Name" : self.nme,
            "Color" : self.color,
            "Seats":self.seats,
            "Features":{
                "Feature 1" : self.feature1,
                "Feature 2" : self.feature2,
                "Feature 3" : self.feature3 }})

class name:
    def __init__(self,firstnme,secondnme):
        self.firstnme = firstnme
        self.secondnme = secondnme
    def Printer(self):
        print( f"{self.firstnme} {self.secondnme}")

class student:
    def __init__(self,nme,school,grade,adress):
        self.nme = nme
        self.school = school
        self.grade = grade
        self.adress = adress
    def Studenter(self):
        print({
            "Name": self.nme,
            "School":self.school,
            "Grade":self.grade,
            "Adress":self.adress})

class Discord:
    def __init__(self,nme,username,pdw):
        self.nme=nme
        self.pdw = pdw
        self.username = username
    def Stuff(self):
        print( {
            "Name":self.nme,
            "Username":self.username,
            "Password" :self.pdw
        })

class bottle:
    def __init__(self,color,size):
        self.color=color
        self.size=size
    def Bottler(self):
        print({
            "Color":self.color,
            "Size":self.size
        })