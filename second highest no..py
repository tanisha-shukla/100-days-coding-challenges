print(".."*90)
print("             SECOND   HIGHEST    NUMBER     ")
print(".."*90)
a = eval(input("ENTER THE LIST OF VALUES :"))

m = 0
for num in a:
    if num > m:
        m = num
res = 0
for num in a:
    if num != m and num > res:
        res = num
print("\nSECOND HIGHEST NUMBER IS :",res)
print(".."*90)
print("DAY - 40 COMPLETED :)")

