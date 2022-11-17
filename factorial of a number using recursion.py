print("-"*100)
print("                        FACTORIAL  OF  A  NUMBER  USING  RECURSION ")
print("-"*100)

def factorial(num):
    if num == 1:
        return 1
    res = num * factorial(num -1)
    return res

n =int(input("\nENTER THE NUMBER :"))
r =factorial(n)
print("\nFACTORIAL OF ",n,"IS",r)

print("-"*100)
print("DAY - 68 COMPLETED :)")
