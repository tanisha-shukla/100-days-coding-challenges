print("-"*100)
print("                        SUM  OF  DIGITS   USING  RECURSION ")
print("-"*100)

def sumofDigit(num):
    if num == 0:
        return 0
    d = num % 10
    num = num // 10
    res = d + sumofDigit(num)
    return res

n =int(input("\nENTER THE NUMBER :"))
r =sumofDigit(n)
print("\nSUM OF DIGITS OF  ",n,"IS :",r)

print("-"*100)
print("DAY - 70  COMPLETED :)")
