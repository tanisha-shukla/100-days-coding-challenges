print("-"*90)
print("         CHECKING A YEAR IS LEAP OR NOT  ")
print("-"*90)
year =eval(input("ENTER A YEAR TO BE CHECKED :"))
print("-"*90)
if year % 100 == 0:
    if year % 400 ==0:
        print(year,"IT IS A LEAP YEAR")
    else:
        print(year,"IT IS NOT  A LEAP YEAR")
else:
    if year % 4 ==0:
        print(year,"IT IS A LEAP YEAR")
    else:
        print(year,"IT IS NOT  A LEAP YEAR")
print("-"*90)
print("DAY 07 COMPLETED :)")
    
