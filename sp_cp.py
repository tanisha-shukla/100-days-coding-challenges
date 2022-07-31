print("-"*90) 
print("                     Y.M.C.A  STORE                                  ")
print("-"*90)
n= input("ENTER A COUSTOMER NAME : ")
cp = eval(input("ENTER A COST PRICE :"))
sp = eval(input("ENTER A SELLING  PRICE :"))
print("-"*90)
if sp > cp :
    print("PROFIT IS Rs.",sp-cp)
elif cp > sp :
    print("LOSS IS Rs.",cp-sp)
else :
    print("NO LOSS NO PROFIT ")
print("-"*90)
print("DAY 10 COMPLETED :) ")
