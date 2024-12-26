print("Statistical Operations on DataFrame in Python Pandas\n")

import pandas as pd


c1=[2200,1100,2300,1700,1800]
c2=[1200,1300,2300,1800,1600]
c3=[1300,2300,2000,1400,1200]

years=['2019','2020','2021','2022','2023']
df = pd.DataFrame({"Years ":years, 'Company A':c1 , 'Company B': c2 , 'Company C' : c3})
print(df)
print(df.describe())

print("\nDAY - 100")
