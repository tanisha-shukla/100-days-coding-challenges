print("Single  Level  Inheritance\n")
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name is ",self.name)
        print("Age is ",self.age)

class Student(Person):
    def __init__(self,name,age,dob):
        self.dob=dob
        super().__init__(name,age)

    def displayInfo(self):
        print(self.name,self.age,self.dob)

p=Person("XYZ",43)
p.display()
o=Student("ABC ",22,"21-09-2008")
o.display()
o.displayInfo()

print("\nDAY - 88")
