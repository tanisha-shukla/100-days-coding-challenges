
print(".."*90)
print("                 LOGIN    SCREEN   USING   CSV  FILE           ")
print(".."*90)

import csv

username =input("ENTER USERNAME :")
password =input("ËNTER PASSWORD :")

f =open("passwords.csv","r")
cr =csv.reader(f)
for row in cr:
    if row[0] == username and row[1] == password:
        print("\nWELCOME ",username,"ACCESS GRANTED !!")
        break
else:
        print("\nINVALID USERNAME OR PASSWORD !!")
f.close()

print(".."*90)
print("DAY - 63 COMPLETED :)")

# FILE CONTAIN (PASSWORDS)
'''
list,Mutable
tuple,Immutable
dictionary,Mutable
Integer,1234
float,12.5
Tanisha,Shukla

'''
