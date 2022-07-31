print("."*100)
print("               PERFECT NUMBER OR NOT                    ")
print("."*100)
num =int(input("ENTER A NUMBER :"))
print("."*100)
p =0
for i in range (1,num):
    if num %i ==0:
        p+=i
       

if num ==p:
    print(num , " IS A PERFECT NUMBER ")
else:
     print(num , " IS  NOT A PERFECT NUMBER ")
print("."*100)
print(" DAY - 14 COMPLETED :) ")
print("."*100)
