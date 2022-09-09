print("-"*150)
print("                                BINARY              SEARCH     ")
print("-"*150)
A =eval(input("ENTER THE NUMBERS OF LIST :"))
A.sort()
print("\nSORTED LIST IS :",A)
print("-"*90)
num = int(input("ENTER THE NUMBER TO BE  SEARCHED :"))
print("-"*90)

beg = 0
end = len(A) -1
while beg <= end:
    mid = (beg + end) // 2
    if A[mid] == num:
        print("\n NUMBER FOUND AT POSITION :", mid+1)
        break
    elif num > A[mid]:
        beg = mid + 1
    elif num < A[mid]:
        end = mid - 1
else:
    print("\n NUMBER NOT FOUND")
print("-"*90)
print("DAY -  35   COMPLETED  :)")

