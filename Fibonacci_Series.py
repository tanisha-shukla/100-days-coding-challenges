print("~"*90)
print("                                 FIBONACCI     SERIES               ")
print("~"*90)
print(" "*90)
n= eval(input("HOW MANY TIMES DO YOU WANT TO PRINT FIBONACCI SERIES :"))

print(" "*90)
a = 0
b=1
s =0
if n>= 2:
    print(a,b , end =' ')
    for i in range (n-2):
            s =a + b
            a =b
            b = s
            print(s, end =' ')
            
print(" "*90)
print(" "*90)

            
print("DAY -18  COMPLETED :) ")
