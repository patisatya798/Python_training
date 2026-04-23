# class Myclass:
#     x = 5
#     print("Hello Satyaranjan")

# p1 = Myclass()
# print(p1.x)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
       print(self.age)
       return self.name
    


p1 = Person("Satya" , 23)
print(p1.name)
print(p1.age)
print(p1.show())