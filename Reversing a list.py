print("~"*150)
print("                       REVERSING   A    LIST            ")
print("~"*150)
a = eval(input("\nENTER A LIST OF VALUES :"))
n = len(a)
for i in range( n // 2):
     a[i],a[n-1-i] = a[n-1-i],a[i]

print("\nREVERSING LIST IS :",a)
print("~"*150)
print("DAY - 36 COMPLETED :)")
