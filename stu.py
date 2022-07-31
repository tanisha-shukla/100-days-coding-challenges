print("-"*90)
print("              STUDENT REPORT CARD                      ")
print("-"*90)

name = input(" ENTER A STIDENT NAME :")
math =eval (input(" ENTER A MARKS OBTAINED IN MATHS : "))
eng =eval (input(" ENTER A MARKS OBTAINED IN ENGLISH  : "))
sci =eval (input(" ENTER A MARKS OBTAINED IN SCIENCE  : "))
sst =eval (input(" ENTER A MARKS OBTAINED IN SOCIAL SCIENCE : "))
sans =eval (input(" ENTER A MARKS OBTAINED IN SANSKRIT  : "))
total  = math +eng + sci +sst + sans
per = total / 5
print("-"*90)
print(" REPORT CARD BELONG  :" , name )
print("-"*90)

print("TOTAL MARKS SCORED :",total)
print("TOTAL PERCENTAGE  :", per ,"%")
print("-"*90)

if per >=40 :
    print("CONGRATULATIONS  !!!!")
else :
    print("SORRY , YOU HAVE TO GIVE REEXAM ")
print("-"*90)
print ("DAY - 03 COMPLETED :)")


