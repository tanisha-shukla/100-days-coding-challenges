import mysql.connector
print("-"*100)
print("             MYSQL  AND   PYTHON   SHOWING  TABLE   DATA                 ")
print("-"*100)

con =mysql.connector.connect(host ="localhost",user ='root',password ="python")
if con.is_connected():
    q ="select * from student "
    cur =con.cursor()
    cur.execute(q)
    res =cur.fetchall()
    for row in res:
        print("ID IS ",row[0],"NAME  IS ",row[1],"AGE IS ",row[2])
    if cur.rowcount == 0:
        print("TABLE IS EMPTY ")
    else:
        print(cur.rowcount," STUDENTS PROCESSED")
else:
    print("ERROR IN CONNECTION ")
    
# REQUIRED ANSWER
'''
ID IS  12 NAME  IS XYZ  AGE IS 21
ID IS  42 NAME  IS pqr  AGE IS 24
ID IS  15 NAME  IS ABC AGE IS 23
ID IS  10 NAME  IS uvw AGE IS 21
4 STUDENTS PROCESSED
'''

print("DAY - 71 COMPLETED :)")
print("-"*100)


