print("↜"*80)
print("                                SELECTION                    SORT          ")
print("↜"*80)

a = eval(input("ENTER  THE   OF  VALUES  : "))
n =len(a)

print("\nBEFORE  SWAP IS  :",a)

for i in range(n - 1):
    for j in range(i+1,n):
        if a[i]  >  a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("\nAFTER  SWAP IS  :",a)
print("↜"*80)
print("DAY - 41  COMPLETED  :) ")


    
