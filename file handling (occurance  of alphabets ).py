print("   QUESTION ON FILE HANDLING  \n")
'''
Sample :- Write a function  AMcount() in python  , which should read each character of a
text file story.txt , should count and display the occurance of alphabets A and M ( including small cases a and m too ).

File contains :- I am a student . I known programming languages like python , c , c++ , java etc.
'''
def AMcount():
    f = open ("story.txt")
    data = f.read()
    print(data)
    cntA = 0
    cntM = 0
    for ch in data :
        if ch == "a" or ch == "A" :
            cntA +=1
        elif ch == "m" or ch == "M" :
            cntM +=1

    print(" A  occurs " , cntA , "   times ")
    print(" M  occurs " , cntM , "   times ")

AMcount()
print(" DAY - 82  COMPLETED  ")
