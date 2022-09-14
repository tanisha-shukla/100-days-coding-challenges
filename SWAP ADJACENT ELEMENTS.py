print("~"*150)
print("                      SWAP  ADJACENT   ELEMENTS                                 ")
print("~"*150)
a =eval(input("ENTER THE LIST OF VALUES :"))
print("\nBEFORE SWAP IS : ",a)
for i in range(0,len(a),2):
    if i+1 < len(a):
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
print("\nAFTER  SWAP IS : ",a)
print("~"*150)
print("DAY - 37 COMPLETED :)")


