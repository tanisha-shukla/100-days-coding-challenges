print("--"*90)
print("                           CHECK   STRENGTH   OF  A  PASSWORD                                       ")
print("--"*90)

password =input("ENTER THE REQUIRED PASSWORD :")

n =len(password)
if n >=8 and n <=16:
    capital =0
    small =0
    digit =0
    special =0
    other =0
    for ch in password:
        if ch.isupper():
            capital +=1
        elif ch.islower():
            small +=1
        elif ch.isdigit():
            digit +=1
        elif ch in ".,!@#$%&*()~?><^" :
            special +=1
        else:
            other +=1
            break
    if other != 0:
        print("\nINVALID PASSWORD")
    else:
        if capital > 0 and small > 0 and digit > 0 and special > 0:
            print("\nSTRONG PASSWORD !!")
        else:
            print("\nWEAK PASSWORD !!")
else:
    print("\nPASSWORD MUST HAVE MINIMUM OF 8 AND MAXIMUM OF 16 CHARACTERS !!")

print("--"*90)
print("DAY - 59 COMPLETED :)")
