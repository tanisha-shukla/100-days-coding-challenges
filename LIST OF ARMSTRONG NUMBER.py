print("."*90)
for num in range(100,10000):
    b = num
    s = 0
    while b >0 :
        d = b %10
        s = s + d **3
        b = b //10

    if s == num :
        print(num, " IS ARMSTRONG NUMBER ")
print("."*90)
print("DAY - 25 COMPLETED :) ")
