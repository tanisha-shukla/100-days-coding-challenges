import mysql.connector

print("-"*100)
print("   MYSQL  AND  PYTHON SEARCHING   A  RECORD ")
print("-"*100)

con =mysql.connector.connect(host ="localhost",user ='root',password ="python")
if con.is_connected():
    am = input("Enter the admission no. of the student  :")
    q = "select * from  student  where admn  = "+ am
    cur1 = con.cursor()
    cur1.execute(q)
    res = curl.fetchone()
    if res != None:
        print(res)
    else:
        print("No  Student Found with given ID  ")


    
    print("STUDENT DELETED SUCCESSFULLY")



print(" DAY 75 COMPLETED :)")
