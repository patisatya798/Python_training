class Company:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def showname(self):
        print(self.name , self.city)

class Employee(Company):
    def __init__(self, name,city,fname,lname):
        super().__init__(name, city)
        self.fname=fname
        self.lname = lname

    def showstudentname(self):
        super().showname()
        print(self.fname , self.lname)

s1 = Employee("Legacore-Informatics",'Bhubaneswar','satya',"pati")
s1.showstudentname()