print("Overload Relational Operators  \n")

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def __str__(self):
        return "Length is {0} , Breadth is {1} ".format(self.l , self.b)


    def __gt__(self,other):
        if self.l*self.b > other.l * other.b:
            return True
        else:
            return False

    def __ge__(self,other):
        return self.l*self.b >= other.l * other.b

    def __lt__(self,other):
        return self.l*self.b < other.l * other.b

    def __le__(self,other):
        return self.l*self.b <= other.l * other.b


    def __eq__(self,other):
        return self.l*self.b == other.l * other.b

    def __ne__(self,other):
        return self.l*self.b != other.l * other.b

p1 =Rectangle(12,34)
p2 =Rectangle(12,148)

print("First Rectangle is ",p1)
print("Second Rectangle  is ",p2)

print("\nComparison Results :- ")
print("p1 > p2 : ",p1>p2)
print("p1 < p2 : ",p1<p2)
print("p1 >= p2 : ",p1>=p2)
print("p1 <= p2 : ",p1<=p2)
print("p1 == p2 : ",p1==p2)
print("p1 != p2 : ",p1!=p2)

'''if p1 > p2:
    print("First Rectangle is  bigger in area")
else:
    print("Second Rectangle  is bigger in area")'''

print("\nDAY - 93")
