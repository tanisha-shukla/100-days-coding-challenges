print("`"*140)
print("                         INSERTION          SORT                   ")
print("`"*140)

a =eval(input("\nENTER THE LIST OF NUMBERS : "))
m =len(a)

print("\nBEFORE SWAP IS : ",a)

for i in range(1,m):

    num = a[i]
    j = i-1
    while j >= 0 and num < a[j]:
        a[j+1] = a[j]
        j -= 1
        a[j+1] = num

print("\nAFTER SWAP IS : ",a,"\n")

print("`"*140)
print("DAY - 43 COMPLETED :)")
