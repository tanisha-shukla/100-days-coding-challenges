print(' FUNCTION QUESTION  \n              ')
'''
Ques - Write a function LShift(Arr , n) in python , which accepts a list Arr of numbers  and n is  a numeric
value by which all elements of the list are shifted to left.
Sample Input Data of the list
Arr = [10,20,30,40,12,11] , n =2
Output
Arr = [30,40,12,11,10,20]
'''
def LShift(Arr , n) :
    # The code will repeat for n times
    for i in range (n) :
        val = Arr.pop(0)  # remove the first element from the list
        Arr.append(val)  #adds same element removed above at the end of the list
        
    print(Arr)

A = [10,20,30,40,12,11]
LShift(A , 2)

print("\nDAY - 79  COMPLETED ")
