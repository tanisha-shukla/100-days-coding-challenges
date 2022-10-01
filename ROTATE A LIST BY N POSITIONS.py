print("^"*90)
print("                ROTATE    A     LIST    BY   N    POSITIONS         ")
print("^"*90)

A =eval(input("ENTER THE LIST OF NUMBERS :"))
n =eval(input("\nENTER THE NUMBER OF POSITIONS TO SHIFT :"))
print("\nLIST OF ELEMENTS :",A)

for i in range(n):
    temp =A[0]
    for j in range(len(A)-1):
        A[j] = A[j+1]
    A[-1] = temp
    
print("\nAFTER THE SHIFT OF POSITIONS :",A)
print("^"*90)
print("DAY - 50 COMPLETED :)")
