print("-"*100)
print("                             NUMBER IS PRIME OR NOT  PRIME                 ")
print("-"*100)
num =int(input("ENTER A NUMBER :"))
print("-"*100)         
f =0
for i in range (1, num +1):
         if  num % i == 0:
             f  += 1
if f ==2:
         print(num , "IS A PRIME NUMBER ")
else:
     print(num , "IS  NOT A PRIME NUMBER ")
print("-"*100)
        
print("DAY - 15 COMPLETED :) ")
