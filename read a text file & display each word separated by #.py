print("..."*90)
print("                 READ  A  TEXT  FILE  AND  DISPLAY  EACH  WORD  SEPARATED  BY  #          ")
print("..."*90)

f =open("record.txt","r")
data = f.readlines()
for lines in data:
    for word in lines.split():
        print(word,end ="#")
    print()
f.close()


# OTHER METHOD
'''
f =open("record.txt","r")
data = f.read().split()

print("#".join(data))
f.close()

'''
# FILE CONTAIN
'''
This is a sample file which  we are creating using a python program.
This file will be used through another program to process its data .
Thank you.
Have a nice day.
'''

print("..."*90)
print("DAY -62 COMPLETED :)")
