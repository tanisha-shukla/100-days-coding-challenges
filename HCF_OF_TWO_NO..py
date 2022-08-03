print(" "*70)
print("        HCF OF TWO NUMBERS                        ")
print(" "*70)
a = int(input("ENTER THE FIRST NUMBER :"))
b = int(input("ENTER THE  SECOND  NUMBER :"))
print(" "*70)
while a % b != 0:
    res = a % b
    a = b
    b = res
print(" HCF  IS " ,b)
print(" "*70)
print("DAY - 17 COMPLETED :)")
