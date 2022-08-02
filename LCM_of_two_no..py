print("~"*90)

print("                LCM  OF  TWO  NUMBERS                                                     ")

print("~"*90)
print("  " *90)
p = int(input(" ENTER A  FIRST NUMBER :"))
q = int(input(" ENTER A  SECOND NUMBER :"))
print("  " *90)
print("~"*90)
print("  " *90)
if p > q:
     a = p
else :
     a = q

for i in range (a, p*q +1):
    if i % p == 0 and i % q ==0:
        print("LCM OF ", p , "AND " , q , " IS " , i )
        break
print("~"*90)
print("  " *90)
print("DAY - 16  COMPLETED :) ")
        
