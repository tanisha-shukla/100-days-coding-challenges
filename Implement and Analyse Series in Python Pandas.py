print("To Implement and Analyse Series in Python Pandas\n")

import pandas as pd

st= {'Abc':90,'Xyz':87,'Pqr':76,'Def':66,'Jkl':99,'Mno':56}
S = pd.Series(st)
print(S)
print(S.size)
print(S.nbytes)
print(S[S >= 80])
print(S + 2)
print(S.sort_values())
print(S.max(),S.min())
print(S.mean())


print("\nDAY - 99")
