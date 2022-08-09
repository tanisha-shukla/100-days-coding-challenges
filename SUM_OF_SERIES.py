print(""*90)
print("         SUM OF SERIES            ")
print(""*90)
n= int(input("ËNTER A NUMBER :"))
print(""*90)
s =0
for i in range(1, n+1):
    if i < n :
        print("1/"+ str(i),end =' + ')
    else:
        print("1/" + str(i))
    s += 1/i
print("SUM OF SERIES : ", round(s,2))
