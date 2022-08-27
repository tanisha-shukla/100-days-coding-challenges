print("~"*90)
print("           TRIANGLE SHAPE                " )
print("~"*90)

n = int(input("ENTER THE NUMBER OF ROWS :"))
for i in range(1,n+1):
     for j in range(n-i):
         print(" ", end = '')
     for p in range(2 * i - 1 ):
         print("*", end = '')
     print()
print("~"*90)
print("DAY - 28 COMPLETED :)")
