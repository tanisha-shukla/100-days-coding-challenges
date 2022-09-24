print(".."*100)
print("                NUMBER    OF   VOWELS      IN    A    STRING                    ")
print(".."*100)
txt =input("\nENTER THE STRING :")
c =0
for ch in  txt:
    if ch in 'aeiouAEIOU':
        c += 1
print("\nNO. OF VOWELS  IN A STRING :",c)

print(".."*100)
print("DAY - 45  COMPLETED :)")
