print("MULTIPLE   INHERITANCE \n")

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth .")

class Animal:
    def  animal_info(self):
        print("Winged animals can flap .")

class Bat(Mammal,Animal):
    def display(self):
        Mammal.mammal_info(self)
        Animal.animal_info(self)


b=Bat()
b.display()
    

print("\nDAY - 91")
