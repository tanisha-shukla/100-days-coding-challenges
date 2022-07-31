from math import *
print("-"*90)
print("        QUADRATIC EQUATIONS                 ")
print("-"*90)
a =eval(input("ENTER A VALUE FOR A :"))
b =eval(input("ENTER A VALUE FOR B :"))
c =eval(input("ENTER A VALUE FOR C :"))
print("-"*90)
d = b**2-4*a*c
print("DISCRIMINANT :" , d)
if d < 0 :
    print("REAL ROOTS DOESNOT EXIST ONLY IMAGINARY ROOTS  EXIST ")
elif d ==0:
    r1 =r2 =-b/(2*a)
    print("  REAL AND EQUAL ROOTS EXITS  ARE  : ",r1, "and", r2)
elif  d >0:
    r1 = round(-b+sqrt(d)/2*a,2)
    r2 = round(-b-sqrt(d)/2*a,2)
    print(" REAL ROOTS  AND UNEQUAL ROOTS ARE EXIST ARE :",r1 ,"and",r2)
else:
    print("INVALID NUMBERS ARE ENTERS :( ")
print("-"*90)
print(" DAY - 05 COMPLETED :) ")

