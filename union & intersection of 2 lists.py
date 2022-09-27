print(".."*150)
print("                         UNION    AND    INTERSECTION    OF   TWO   LISTS                         ")
print(".."*150)

a =eval(input("ENTER THE FIRST LIST :"))
b =eval(input("ENTER THE SECOND  LIST :"))

c =a.copy()
i =[]

print(".."*150)

for val in b:
    if val in a:
        i.append(val)
    else:
        c.append(val)
print("\nUNION OF LIST IS :",c)
print("\nINTERSECTION OF LIST IS :",i)
print(".."*150)
print("DAY - 48 COMPLETED :)")

