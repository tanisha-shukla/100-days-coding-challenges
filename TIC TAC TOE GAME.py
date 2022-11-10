print("⇠"*70)
print("                           TIC    TAC   TOE                 ")
print("⇠"*70)

grid ={1 :' ',2:' ',3:' ',4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

def show():
    print()
    print("-"*30)
    print("|    "+grid[1]+"   |    "+grid[2]+"      |    "+grid[3]+"       |   ")
    print("-"*30)
    print("|    "+grid[4]+"   |    "+grid[5]+"      |    "+grid[6]+"      |   ")
    print("-"*30)
    print("|    "+grid[7]+"   |    "+grid[8]+"      |    "+grid[9]+"      |   ")
    print("-"*30)
    print()


player1 =input("\nENTER PLAYER 1's NAME :")
player2 =input("ENTER PLAYER 2's NAME :")

turn =1

while True:
    show()
    if turn % 2 ==1:
        pos =int(input(player1+" ENTER THE POSITION TO PLACE  ~ X :"))
        if pos in grid and grid[pos] ==" ":
            grid[pos] = "X"
            turn += 1

    else:
            pos = int(input(player2 + " ENTER THE POSITION TO PLACE  ~ O :"))
            if pos in grid and grid[pos] == " ":
                grid[pos] = "O"
                turn += 1

    if grid[1] == grid[2] == grid[3] and grid[1] != " ":
            if grid[1] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[4] == grid[5] == grid[6] and grid[4] != " ":
            if grid[4] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[7] == grid[8] == grid[9] and grid[7] != " ":
            if grid[7] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[1] == grid[4] == grid[7] and grid[7] != " ":
            if grid[1] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[2] == grid[5] == grid[8] and grid[2] != " ":
            if grid[2] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[3] == grid[6] == grid[9] and grid[3] != " ":
            if grid[3] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[1] == grid[5] == grid[9] and grid[1] != " ":
            if grid[1] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif grid[3] == grid[5] == grid[7] and grid[7] != " ":
            if grid[3] =="X":
                print(player1 ,"WINS !!")
            else:
                print(player2 ,"WINS !!")
            show()
            break
    elif turn >9:
            print("\nIT's DRAW ")
            show()
            break

print("⇠"*70)
print("DAY - 65 COMPLETED :)")


