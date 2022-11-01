class janator:
    def __init__(self,salary):
        self.salary = salary
    def Cleaner(self):
        print("Cleans Table no. 17")
    def Salay(self):
        print("*Goes To Manager*")
        print(f"Take salary of {self.salary}")

class Chef:
    def __init__(self,salary):
        self.salary = salary
    def cooking(self):
        print("*Cooks Chicken* \n *Gives To Waitor*")
    def Saly(self):
        print("*Goes To Manager*")
        print(f"Take salary of {self.salary}")

class Waitor:
    def __init__(self,salary):
        self.salary = salary
    def Order(self):
        print("*Takes Order* \n *Gives To Chef*")
    def Deliver(self):
        print("*Takes The Food* \n *Gives The Food*")