print("Default and Parameterised constructors ")

class Triangle:
    def __init__(self,x,y,z):  # parameterised 
        self.s1 = x
        self.s2 = y
        self.s3 = z

    def show(self):
        print("Side 1 is : ",self.s1)
        print("Side 2 is : ",self.s2)
        print("Side 3 is : ",self.s3)


t1 =Triangle(7,12,9)
t2=Triangle(3,6,4)
t1.show()
t2.show()

print("DAY - 87")

'''
 def __init__(self):  # default
        self.s1 = 1
        self.s2 = 3
        self.s3 = 2

    def show(self):
        print("Side 1 is : ",self.s1)
        print("Side 2 is : ",self.s2)
        print("Side 3 is : ",self.s3)


t1 =Triangle()
t2=Triangle()
t1.show()
t2.show()
'''

