print("."*100)
print("           FACTORS OF A  NUMBER               ")
print("."*100)
a = int(input("ENTER A NUMBER :"))
print("                   FACTORS OF " ,a, "ÄRE : ")
print(" "*90)
for i in range (1,a+1):
    if a%i ==0:
        print(i)
print("."*100)
print("DAY - 13 COMPLETED :)")
