print("--"*90)
print("                     SEARCH    AND    UPDATE   A   DICTIONARY                                 ")
print("--"*90)
def create(emp,n):
    for i in range(n):
        ename =input("\nENTER A EMPLOYEE NAME :")
        sal =int(input("ENTER THE SALARY :"))
        print("\n")
        emp[ename] =sal

def search(emp,nam):
    if name in emp:
        print("CURRENT SALARY IS : ",emp[name])
        emp[name] +=emp[name] *25 / 100
        print("SALARY UPDATED !!")
    else:
        print("NO EMPLOYEE FOUND WITH GIVEN NAME ")

emp={}

n =int(input("\n"
             "HOW MANY EMPLOYEES  ARE THERE :"))
create(emp,n)
print("EMPLOYEE DICTIONARY IS :",emp)

name =input("\nENTER EMPLOYEE NAME WHOSE SALARY HAS TO BE INCREASED :")
search(emp,name)
print("\nEMPLOYEE DICTIONARY IS :",emp)



print("--"*90)
print("DAY - 52 COMPLETED :)")
