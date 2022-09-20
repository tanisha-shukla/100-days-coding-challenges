print("-|"*100)
print("                                BUBBLE            SORT          ")
print("-|"*100)

a = eval(input("\nENTER  THE   OF  VALUES  : "))
n =len(a)

print("\nBEFORE  SORT IS  :",a)

for i in range(n - 1):
    for j in range(0,n-1-i):
        if a[j]  >  a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("\nAFTER  SORT IS  :",a)
print("-"*100)
print("DAY - 42  COMPLETED  :) ")

