print("-"*150)
print("               LINEAR       SEARCH   ")
print("-"*150)
list =eval(input("ENTER A LIST OF NUMBER :"))
num =eval(input("\nENTER A  NUMBER TO BE SEARCHED :"))
print("-"*150)
count = 0
for i in range(len(list)):
    if list[i] == num :

        print("\nNUMBER FOUND AT POSITION ",i+1)
        count += 1
if count == 0:
    print("NUMBER NOT FOUND ")
print("-"*150)
print("DAY - 34 COMPLETED :)")
