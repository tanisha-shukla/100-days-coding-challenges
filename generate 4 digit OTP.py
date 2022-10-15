print("--"*90)
print("                  GENERATING     FOUR    DIGITS   OTP (ONE TIME PASSWORD)")
print("--"*90)
import random as rd
def generateOTP():
    otp =[]
    i =0
    while i < 4:
        digit = rd.randint(0,9)
        if digit not in otp:
            otp.append(digit)
            i +=1
    return otp

otp = generateOTP()
print("\nYOUR OTP IS :",end =' ')
for d in otp:
    print(d,end=' ')

print("\n")
print("--"*90)
print("\nDAY - 56 COMPLETED :)")

