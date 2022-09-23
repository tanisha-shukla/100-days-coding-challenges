print("."*250)
print("                      PALINDROME       OF               STRING        ")
print("."*250)
st = input("\nENTER A STRING : ")

res = ""
for i in range(len(st)-1,-1,-1):
    res += st[i]
print("\nSTRING IS :",st)
print("\nREVERSE  STRING IS : ",res)
if st == res:
    print("\nIT IS A PALINDROME")
else:
    print("\nIT IS NOT  A PALINDROME")

print("."*250)
print("DAY - 44 COMPLETED :)")
