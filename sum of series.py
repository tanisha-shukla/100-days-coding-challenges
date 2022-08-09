print("-"*90)
print("          SUM OF SERIES         ")
print("-"*90)
a = int(input(" ENTER A  VALUE OF X  :"))
n =int(input(" ENTER A  VALUE OF N  :"))
print("-"*90)
s = 0
for i in range(1, n+1):
    if i < n:
        print(str(a)+"^"+str(i), end =' + ')
    else:
        print(str(a) + "^" + str(i))
    s += a**i
print("SUM OF SERIES IS :",s )
print("-"*90)
print(" DAY - 22  COMPLETED :)")

