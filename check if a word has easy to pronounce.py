print("-"*90)
print("                       CHECK  IF  A  WORD  HAS  EASY  TO   PRONOUNCIATION                          ")
print("-"*90)

word =input("\nENTER A WORD :")
c =0
for ch in word :
    if ch.isalpha():
        if ch not in 'aeiouAEIOU':
            c += 1
            if c == 4:
                print("\nIT IS DIFFICULT TO PRONOUNCE ")
                break
        else:
            c =0
    else:
        print("\nINVALID INPUT \n")
        break
else:
    print("\nIT IS EASY TO PRONOUNCE \n")

print("-"*90)
print("DAY - 67 COMPLETED :)")


# WORDS CONTAIN
'''
PYTHON
PYCHARM
CRYPT
FLYBY
HMMM
MYTHS
LYMPH
'''
