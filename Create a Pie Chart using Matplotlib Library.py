print("Create a Pie Chart using Matplotlib Library ")

import matplotlib.pyplot as plt

subjects=['Full Stack ','Cyber Security','Sotware ','Enterpreneurship','Higher Study','Govt. Job']
students=[39,15,22,6,8,10]
plt.pie(students,colors=['olive','grey','teal','green','tan','pink'],autopct ="%.0f%%" , wedgeprops={"edgecolor":"black"}, labels=subjects)
plt.title("Student Opting for  COURSES")
plt.legend(loc='upper left')
plt.show()

print("DAY - 96 ")

