print("--"*90)
print("                     VALIDATE  PHONE  NO.  ENTERED  BY USER                                     ")
print("--"*90)
def isphoneValid(phone):
    if len(phone) != 10:
        return False
    elif not phone.isdigit():
        return False
    elif phone[0] not in("689"):
        return False
    else:
        return True

text =input("ENTER PHONE NUMBER :")
if isphoneValid(text):
    print("\nPHONE NUMBER IS VALID !!")
else:
    print("\nPHONE NUMBER IS INVALID !!")


print("--"*90)
print("DAY - 58 COMPLETED :)")
