print("~~"*90)
print("        REMOVE   DUPLICATES   FROM   EXISTING   LIST                  ")
print("~~"*90)

a = eval(input("ENTER A LIST OF VALUES : "))
i =0
print("\nBEFORE  REMOVE LIST IS : ",a)
while i < len(a):
    if a.count(a[i]) > 1:
        a.remove(a[i])
    else:
        i +=1

print("\nAFTER  REMOVE LIST IS : ",a)
print("~~"*90)
print("DAY - 39 COMPLETED :)")
