print("-"*100)
print("                            TOGGLE      CASE    A    STRING             ")
print("-"*100)

txt =input("\nENTER A STRING :")

res =''
for ch in txt:
    if ch.islower():
        res +=ch.upper()
    elif ch.isupper():
        res +=ch.lower()
    else:
        res +=ch

print("\nORIGINAL STRING :",txt)
print("\nRESULTANT STRING :",res)

'''OTHER METHOD
     res =txt.swapcase()  '''

print("-"*100)
print("DAY - 54 COMPLETED :)")

