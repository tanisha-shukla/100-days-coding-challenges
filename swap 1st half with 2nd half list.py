print("~"*150)
print("                      SWAP   FIRST  HALF  OF  LIST  WITH  SECOND  HALF            ")
print("~"*150)
a =eval(input("ENTER THE LIST OF VALUES :"))
print("\nBEFORE SWAP IS : ",a)
n = len(a)

if n % 2 == 0:
    gap = n // 2
else :
    gap = n // 2 + 1

for i in range(n//2):
    temp = a[i]
    a[i] = a[i+gap]
    a[i+gap] = temp
print("\nAFTER  SWAP IS : ",a)
print("~"*150)
print("DAY - 38 COMPLETED :)")


