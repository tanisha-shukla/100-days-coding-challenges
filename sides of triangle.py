print("-"*90)
print("               SIDES OF TRIANGLES             ")
print("-"*90)
a=eval(input("ENTER A FIRST SIDE OF TRIANGLE :"))
b=eval(input("ENTER A SECOND SIDE OF TRIANGLE :"))
c=eval(input("ENTER A THIRD SIDE OF TRIANGLE :"))
print("-"*90)
if a==b and b==c:
    print("TRIANGLE IS EQUILATERAL ")
elif a==b or b==c or c==a :
    print("TRIANGLE IS ISOSCELES")
else:
    print("TRIANGLE IS SCALENE")
print("-"*90)
print("DAY O8 COMPLETED :)")
