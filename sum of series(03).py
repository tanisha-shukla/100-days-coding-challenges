print("-"*90)
print("    SUM    OF  SERIES ")
print("-"*90)
a = int(input(" ENTER A VALUE OF X :"))
n = int(input(" ENTER A VALUE OF  N :"))
print("-"*90)
s = 0
p = 1
for i in range(1, n+1):
    p = p*i
    s = s +  a ** i / p
print("SUM OF SERIES IS :",round(s,2))
print("-"*90)
print("DAY - 23 COMPLETED :)")


