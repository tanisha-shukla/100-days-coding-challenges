
import mysql.connector

print("-"*100)
print("   MYSQL  AND  PYTHON  DELETING   A  RECORD ")
print("-"*100)

con =mysql.connector.connect(host ="localhost",user ='root',password ="python")
if con.is_connected():
    rno = input("ENTER ROLL NO OF STUDENT TO BE DELETED  :")
    q = "delete from  student  where sid  = "+ rno
    cur1 = con.cursor()
    cur1.execute(q)
    con.commit()
    print("STUDENT DELETED SUCCESSFULLY")

# REQUIRED  OUTPUT
'''
ENTER ROLL NO OF STUDENT TO BE DELETED :  121 
STUDENT DELETED SUCCESSFULLY
'''

print(" DAY 74 COMPLETED :)")
