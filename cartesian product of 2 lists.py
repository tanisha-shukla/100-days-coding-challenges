print("^^"*50)
print("                CARTESIAN          PRODUCT       OF      TWO     LISTS            ")
print("^^"*50)
A =eval(input("\nENTER THE FIRST  LIST OF NUMBERS :"))
B =eval(input("\nENTER THE SECOND  LIST OF NUMBERS :"))

RES =[]
for n1 in A:
    for n2 in B:
        RES.append((n1,n2))

print("\nCartesaian Products Are :",RES)

print("^^"*50)
print("DAY - 49 COMPLETED  :)")
