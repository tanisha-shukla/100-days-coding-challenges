print("Create a Multiple Bar Graphs in Single Plot Area  using Matplotlib Library ")

import matplotlib.pyplot as plt
import pandas as pd

c1=[2200,1100,2300,1700,1800]
c2=[1200,1300,2300,1800,1600]
c3=[1300,2300,2000,1400,1200]

years=['2019','2020','2021','2022','2023']

df = pd.DataFrame({"Years ":years, 'Company A':c1 , 'Company B': c2 , 'Company C' : c3})
df.index = df ["Years "]
df.plot(kind='bar',color=['green','olive','teal','tan','grey'])


plt.title("Sale  Records  over 2019-2023")
plt.xlabel("Sale year ")
plt.ylabel("Sales in Lakhs INR")
plt.grid(True)
plt.show()

print("DAY - 98 ")

