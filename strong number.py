print("              CHECK IF A NUMBER IS STRONG NUMBER OR NOT   ")
print("    ")
import math
num = int(input("Enter a number :"))
print("    ")
s = 0
a = num
while num > 0:
     d = num % 10
     s += math.factorial(d)
     num = num // 10
     
print("    ")
print("Sum is  ", s)
print("    ")
if s == a :
    print("Strong  Number ")
else:
     print(" Not a Strong  Number ")
print("    ")
print(" DAY  - 77 COMPLETED ")
     
 
