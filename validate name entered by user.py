print("--"*80)
print("                     VALIDATE    NAME    ENTERED    BY    USER              ")
print("--"*80)

def validNAME(name):
    for ch in name:
        if not(ch.isalpha() or ch ==' '):
            return False
    else:
        return True

text =input("\nENTER THE NAME TO VALIDATE :")
print("\n")
if validNAME(text):
    print(text + " IS  A VALID NAME ")
else:
    print(text + " IS NOT A  VALID NAME ")

print("--"*80)
print("\nDAY - 57 COMPLETED :)")
