print(".."*100)
print("                       DICTIONARY      FOR      EMPLOYEE                         ")
print(".."*100)
def create(emp,n):
    for i in range(n):
        ename =input("\nENTER A EMPLOYEE NAME :")
        sal =int(input("ENTER THE SALARY :"))
        job =input("ENTER YOUR  JOB NAME :")
        print("\n")
        emp[ename] =[sal,job]
    
emp={}
n =int(input("\nHOW MANY EMPLOYEES  ARE THERE :"))
create(emp,n)
print("EMPLOYEE DICTIONARY IS :",emp)

print(".."*100)
print("DAY - 51 COMPLETED :)")
