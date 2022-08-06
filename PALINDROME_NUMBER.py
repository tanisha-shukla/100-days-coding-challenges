print("-"*90)
print("   CHECK  PALINDROME   NUMBER  ")
print("-"*90)
num = int(input("ENTER A NUMBER TO BE CHECKED : "))
print(" "*90)
a = num
res = 0
while num > 0:
    d = num % 10
    res =  res *10 + d
    num =num //10
print("REVERSE NUMBER IS ",res)
print(" "*90)
if a  ==res:
    print(a , "IS A PALINDROME  NUMBER ")
else:
    print(a , "IS  NOT  A  PALINDROME  NUMBER ")
print("-"*90)
print("DAY - 20 COMPLETED  :)")
    
