import pickle
import os
print("-"*90)
print("                   CONTACT   BOOK  ")
print("-"*90)

def addcontact():
    name =input("ENTER YOUR  NAME :")
    phone =input("ENTER PHONE NO. :")
    data =[name,phone]
    f= open("contacts.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("\nADDED  SUCCESSFULLY !!")

def display():
    f= open("contacts.dat","rb")
    print("-" * 90)
    print("NAME\t\tCONTACT")
    try:
        while True:
            data =pickle.load(f)
            print(data[0]+"\t\t"+data[1])


    except:
        f.close()
        print("-" * 90)


def search():
    name =input("\nENTER NAME TO BE SEARCHED :")
    f = open("contacts.dat", "rb")
    print("-" * 90)
    n =0
    print("NAME\t\tCONTACT")
    try:
        while True:
            data = pickle.load(f)
            if data[0] ==name:
                print(data[0] + "\t\t" + data[1])
                print("-" * 90)
                n +=1
    except:
        if n ==0:
            print("\nNO SUCH CONTACT FOUND !!\n")
        f.close()

def update():
    name = input("\nENTER NAME TO BE UPDATED :")
    f = open("contacts.dat", "rb")
    g = open("tempo.dat", "wb")
    print("-" * 90)
    n = 0
    print("NAME\t\tCONTACT")

    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0] + "\t\t" + data[1])
                print("-" * 90)
                phone =input("\nENTER THE MODIFIED PHONE NO. :")
                data[1] =phone
                n += 1
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("NO SUCH CONTACT FOUND !!\n")
        else:
            os.remove("contacts.dat")
            os.rename("tempo.dat","contacts.dat")

def delete():
    name = input("\nENTER NAME TO BE DELETED :")
    f = open("contacts.dat", "rb")
    g = open("tempo.dat", "wb")
    print("-" * 90)
    n = 0
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print("\nDELETED RECORD  "+data[0] + "\t\t" + data[1])
                n += 1
            else:
                pickle.dump(data, g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("NO SUCH CONTACT FOUND !!\n")
        else:
            os.remove("contacts.dat")
            os.rename("tempo.dat", "contacts.dat")

while True:
    print("\nPRESS 1 -ADD A NEW CONTACT ")
    print("PRESS 2 -DISPLAY ALL CONTACTS ")
    print("PRESS 3 -SEARCH A CONTACT ")
    print("PRESS 4-UPDATE A CONTACT ")
    print("PRESS 5 -DELETE A  CONTACT ")
    print("PRESS ANY OTHER NUMBER TO EXIT  ")

    choi =int(input("\nENTER YOUR CHOICE :"))
    if choi ==1:
        addcontact()
    elif choi ==2:
        display()
    elif choi ==3:
        search()
    elif choi ==4:
        update()
    elif choi ==5:
        delete()
    else:
        break

print("-"*90)
print("DAY - 64 COMPLETED :)")












