print("Create a Histogram for Frequency Distribution  using Matplotlib Library ")

import matplotlib.pyplot as plt

ages=[22,34,45,45,50,32,34,65,50,66,72,41,52,62,70,
          26,44,69,60,87,35,34,29,54,57,56,77,47,48]
bins=[20,30,40,50,60,70,80,90]
plt.hist(ages,bins=bins,color='grey',edgecolor='black')
plt.title(" Health Issues in 2024")
plt.xlabel("Age Of Patients ")
plt.ylabel("Number Of Patients ")
plt.grid(True)
plt.show()

print("DAY - 97 ")

