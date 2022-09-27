print("."*150)
print("                      REVERSE  A   STRING   WORD   BY   WORD    ")
print("."*150)
txt =input("\nENTER THE STRING TO BE REVERSED :")

obj =txt.split()
obj =obj[::-1]
print('\n',obj)

res=''
for i in obj:
    res  += i +"  "
print('\n',res)

''''OTHER METHOD 
res = '  '.join(obj)
print(res)'''

print("."*150)
print("DAY - 47 COMPLETED :)")
