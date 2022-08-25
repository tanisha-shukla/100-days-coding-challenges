print("-"*90)
print("       ITERATIONS OF FOR LOOP    ")
print("-"*90)

n =int(input("ENTER THE  NUMBER  OF ROWS :"))
print("-"*90)
for i in range ( 1, n+1):
    for p in range(1, i+1):
        print(p, end = '')
    print()
print("-"*90)
print(" DAY - 26 COMPLETED :)")
