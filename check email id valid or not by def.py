print("--"*90)
print("                 CHECK   IF   EMAIL-ID   IS   VALID   OR   NOT                        ")
print("--"*90)

def isvalidemail(email):
    if email.endswith(".com"):
        if email[0] != '@' and email.count("@") == 1:
            for ch in email:
                if ch.isalpha() or ch.isdigit() or ch == "_" or ch == "@" or ch == ".":
                    continue
                else:
                    return False
            else:
                return True

        else:
            return False

    else:
        return False
email =input("\nENTER A EMAIL - ID :")

if isvalidemail(email):
    print("VALID EMAIL - ID ")
else:
    print("\nNVALID EMAIL - ID ")

print("--"*90)
print("DAY - 55 COMPLETED :)")

