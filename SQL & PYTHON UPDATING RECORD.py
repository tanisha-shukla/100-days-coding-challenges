import mysql.connector

print("-"*100)
print("   MYSQL  AND  PYTHON  UPDATING   A  RECORD ")
print("-"*100)

con =mysql.connector.connect(host ="localhost",user ='root',password ="python")
if con.is_connected():
    rno = int(input("ENTER ROLL NO OF STUDENT TO BE UPDATED  :"))
    name = input("ENTER NEW NAME :")
    age = int(input("ENTER  NEW AGE :"))
    q = "update student set sname =%s, age = %s where sid = %s"
    values = (rno, name, age)
    cur1 = con.cursor()
    cur1.execute(q, values)
    con.commit()
    print("STUDENT UPDATED SUCCESSFULLY")
    
# REQUIRED ANSWER
'''
ENTER ROLL NO OF STUDENT TO BE UPDATED  :102
ENTER NEW NAME :XYZ
ENTER  NEW AGE :23
STUDENT UPDATED SUCCESSFULLY
'''
print("-"*100)
print("DAY - 73 COMPLETED :) ")
