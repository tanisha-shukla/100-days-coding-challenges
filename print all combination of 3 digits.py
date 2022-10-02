print("--"*90)
print("                 ALL     COMBINATIONS      OF    3    DIGITS                      ")
print("--"*90)

A =[0,0,0]
A[0] =int(input("ENTER FIRST DIGIT :"))
A[1] =int(input("ENTER SECOND DIGIT :"))
A[2] =int(input("ENTER THIRD DIGIT :"))

print("\nNUMBERS ARE :-")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                print(A[i],A[j],A[k])

print("--"*90)
print("DAY - 50 COMPLETED  :)")
