print("--"*90)
print("                    COUNT   THE   FREQUENCY   OF  EACH  LETTER  IN  A  STRING                               ")
print("--"*90)

text =input("\nENTER A STRING :")
dict ={}

for ch in text:
    if ch not in dict:
        dict[ch] = 1
    else:
        dict[ch] += 1
for p in dict:
    print(p,"OCCURS FOR ",dict[p]," TIMES")

print("--"*90)
print("DAY - 53 COMPLETED :)")
