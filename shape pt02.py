print("-"*90)
print("        SHAPE PT.02(USING FOR LOOP)  ")
print("-"*90)
n= int(input("HOW MANY  LINES ARE THERE :"))
print(""*90)
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b or a + b == n + 1 or a == 1 or a == n or b == 1 or b == n :
            print("*",end = " ")
        else:
            print(" ",end =" ")
    print()
print("-"*90)
print(" DAY - 31 COMPLETED :)")
