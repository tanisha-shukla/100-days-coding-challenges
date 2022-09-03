import random as  rd
import time as t
print("."*90)
print("             DICE GAME                                      " )
print("."*90)
a =input("ENTER A NAME OF PLAYER 1 :")
b =input("ENTER A NAME OF PLAYER 2 :")
print("."*90)

val1 = rd.randint(1,6)
val2 =rd.randint(1,6)
t.sleep(2)
print("PLAYER 1 GOT :",val1)
t.sleep(2)
print("PLAYER 2 GOT :",val2)
t.sleep(2)
print("."*90)
if val1 > val2 :
    print("YEHH",a,"WINS")
elif val2 > val1 :
    print("YEHH",b,"WINS")
else:
    print("IT IS A DRAWN")
print("."*90)
print("DAY - 32 COMPLETED :)")


