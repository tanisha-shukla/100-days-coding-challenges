print("-"*60)
print("      SHAPE (USING  FOR LOOP) ")
print("-"*60)
p = int(input("HOW MANY ROWS ARE THERE :"))
print("-"*60)
for a in range(p,0,-1):
    for b in range(a):
        print("*", end ="")
    for s in range(2*(p-a)):
        print(" ",end ="")
    for b in range(a):
        print("*",end="")
    print()
for a in range(1,p+1):
    for b in range(a):
        print("*", end ="")
    for s in range(2*(p-a)):
        print(" ",end ="")
    for b in range(a):
        print("*",end="")
    print()
print("-"*60)
print("DAY - 30 COMPLETED :)")
