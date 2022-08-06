print("~"*90)
print("                                 SUM  OF  DIGITS  OF  A  NUMBER               ")
print("~"*90)
print(" "*90)
n= eval(input("ENTER A NUMBER  :"))
print(" "*90)
s = 0
a = n
while  n>0 :
    d = n % 10
    s +=d
    n = n //10
print("SUM OF DIGIT  OF ",a , "IS " , s)
print("~"*90)
print("DAY - 19 COMPLETED :) ")
