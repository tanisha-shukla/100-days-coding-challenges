print(".."*120)
print("                      OPERATION       ON      STRINGS        ")
print(".."*120)
txt =input("\nENTER THE STRING :")
c =0
a =0
s =0
d =0
for ch in  txt:
    if ch in 'aeiouAEIOU':
        c += 1
    if ch.isalpha() :
        a +=1
    if ch.isspace():
        s +=1
    if ch.isdigit() :
        d += 1
print("\nNO. OF VOWELS  IN A STRING :",c)
print("\nNO. OF  ALPHABETS  IN A STRING :",a)
print("\nNO. OF SPACES  IN A STRING :",s)
print("\nNO. OF DIGITS  IN A STRING :",d)

print(".."*120)
print("DAY - 46  COMPLETED :)")
