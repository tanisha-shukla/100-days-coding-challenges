print("-"*100)
print("                        HCF  OF  TWO   NUMBERS  USING  RECURSION ")
print("-"*100)

def hcf(num1,num2):
   rem =num1 %num2
   if rem == 0:
       return num2
   res =hcf(num2,rem)
   return res

n =int(input("\nENTER THE FIRST NUMBER :"))
m =int(input("\nENTER THE SECOND NUMBER :"))

res =hcf(n,m)
print("\nHCF OF ",n," AND ",m," IS : ",res)

print("-"*100)
print("DAY - 69 COMPLETED :)")

