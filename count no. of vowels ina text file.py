print("/"*90)
print("                  COUNT NUMBER OF VOWEL IN A TEXT FILE        ")
print("/"*90)

f =open("record.py","r")
data =f.read()
print(data)
vowels =0

for ch in data:
    if ch in "aeiouAEIOU":
        vowels +=1
print("\nNO. OF VOWELS IS :",vowels)
f.close()


print("/"*90)
print("DAY - 61 COMPLETED :)")

# FILE CONTAIN 
'''
f=open("record.txt","w")
f.write("This is a sample file which  we are creating using a python program.\n")
f.write("This file will be used through another program to process its data .\n")
f.write("Thank you.\n")
f.write("Have a nice day")
f.close()


'''
