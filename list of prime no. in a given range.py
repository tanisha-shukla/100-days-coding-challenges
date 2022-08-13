print("-"*90)
print("     PRIME    NUMBERS ")
print("-"*90)
start = int(input("ENTER THE STARTING NUMBER :"))
stop = int(input("ENTER THE  ENDING  NUMBER :"))
print("-"*90)
for i in range(start  , stop+1):
    for a in range(2, i):
          if  i % a ==0:
              break
    else:
            print(i," IS PRIME NO.")
print("-"*90)
print(" DAY - 24 COMPLETED :)")

      
      
