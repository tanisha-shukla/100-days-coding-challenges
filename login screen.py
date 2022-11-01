print("//"*90)
print("                      LOGIN     SCREEN     ")
print("//"*90)

for i in range(3):
    userid =input("\nENTER THE USER ID :")
    password =input("\nENTER THE PASSWORD :")

    if userid.lower() =="tanisha" and password.lower() =="python":
        print("\nPASSWORD MATCHED !!!!")
        print("\nACCESS GRANTED")
        break
    else:
        print("\nINVALID USER ID OR PASSWORD")
else:
    print("\nACCESS DENIED")

print("//"*90)
print("DAY - 60 COMPLETED :)")

