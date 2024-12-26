print("Create a Line Chart using Matplotlib Library ")

import matplotlib.pyplot as plt

c1=[2200,1100,2300,1700,1800]
c2=[1200,1300,2300,1800,1600]
years=['2019','2020','2021','2022','2023']
plt.plot(years,c1,color='olive',label='Company A')
plt.plot(years,c2,color='teal',label='Company B')
plt.legend(loc='upper right')
plt.title("Sale  Records  over 2019-2023")
plt.xlabel("Sale year ")
plt.ylabel("Sales in Lakhs INR")
plt.grid(True)
plt.show()

print("DAY - 95 ")

