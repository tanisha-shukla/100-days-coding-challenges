print("-"*90)
print("        ELECTRICITY BILLS                     ")
print("-"*90)
n =input("ENTER A COUSTOMER NAME  :")
print("-"*90)
units =eval(input("ENTER THE NUMBER OF UNIT CONSUME :"))
if units <200:
    bill =4*units
elif units <500:
    bill =800+(units - 200)*6
elif units <800:
    bill = 800 + 1800 +(units -500)*8
else:
    bill =800 +1800+2400 +(units -800)*10
print("ËLECTRICITY BILLS ARE :","Rs.",bill)
print("-"*90)
print("DAY 06 COMPLETED :)"  ) 
