print(" ⁛ "*80)
print("                    GUESS     THE     NUMBER    ")
print(" ⁛ "*80)
import random as rd
num = rd.randint(10,100)
print("-"*150)
n = int(input("HOW MANY TIMES  DO YOU WANT TO REPEAT THE LOOP  :"))
print("-"*150)
for i in range(n):
    guess =int(input("ENTER THE NUMBER BETWEEN  10 TO 100 :"))
    if guess == num:
        print("  YOU WIN    ")
        print("-" * 150)
        break
    elif num > guess:
        print("\n SORRY , THE  NUMBER IS GREATER  THAN YOUR GUESS\n")
        print("-" * 150)
    elif num < guess:
        print("\n SORRY , THE  NUMBER IS SMALLER THAN YOUR GUESS\n")
        print("-" * 150)
else:
    print("YOU LOOSE ~ NEXT TIME YOU MAY WON")
    print("-"*150)
print(" ⁛ "*80)
print("DAY - 33 COMPLETED :)")
