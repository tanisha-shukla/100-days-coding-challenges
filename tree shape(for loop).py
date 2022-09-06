print("~"*90)
print("           TREE SHAPE                " )
print("~"*90)

n = int(input("ENTER THE NUMBER OF ROWS :"))
print("~"*90)
for i in range(1,n+1):
     for j in range( n - i ):
         print("  ", end = ' ')
     for p in range(2 * i - 1 ):
         print(" * ", end = ' ')
     print()
for b in range(n):
    for c in range(2 * (n - 3)):
        print(" ",end =' ')
    print(" *   *   * ")
print("~"*90)

