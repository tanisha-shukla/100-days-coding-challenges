num =int(input(" Enter a number : "))
squ = num ** 2

print("Square is  ", squ)
if str(squ).endswith(str(num)):
    print("An Automorphic  Number ")
else:
     print(" Not  an Automorphic  Number ")
     
print("    ")
print(" DAY  - 78  COMPLETED ")



# ALTERNATIVE
'''a = int(input("Enter the upper limit  :"))
for num in range (1 , a+1):
     sq = num ** 2
     n = len(str(num))
     end = sq % 10 ** n


     if end  == num :
         print (num)      '''
