import mysql.connector

print("-"*100)
print("   MYSQL  AND  PYTHON  INSERTING   A  RECORD ")
print("-"*100)

con =mysql.connector.connect(host ="localhost",user ='root',password ="python")
if con.is_connected():
    rno =int(input("ENTER ROLL NO :"))
    name =input("ENTER NAME :")
    age =int(input("ENTER AGE :"))
    q ="insert into student values(%s,%s,%s)"
    values =(rno,name,age)
    cur1 =con.cursor()
    cur1.execute(q,values)
    con.commit()
    print("STUDENT INSERTED SUCCESSFULLY")
    
# REQUIED ANSWER 
'''
ENTER ROLL NO :26
ENTER NAME :XYZ
ENTER AGE :12
STUDENT INSERTED SUCCESSFULLY
'''
print("-"*100)
print("DAY - 72 COMPLETED :)")
