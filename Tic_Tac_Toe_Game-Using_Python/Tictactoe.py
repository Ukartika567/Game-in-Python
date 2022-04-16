def print_board(board):
    print("",board[1]," │",board[2]," │ ",board[3]," ")
    print("────┼────┼────")
    print("",board[4]," │",board[5]," │ ",board[6]," ")
    print("────┼────┼────")
    print("",board[7]," │",board[8]," │ ",board[9]," ")
    
# for display the instruction of game
def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(position)
    print()
    
    players[0] = input("Player 1-> Please enter your name  : ")
    players[1] = input("Player 2 -> Please enter your name : ")
    
    print("\n-------- Instructions ---------")
    print("->",players[0],"you will using X")
    print("->",players[1],"you will using 0")
    print("-> Turn starts from",players[0])
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("-> press S to start the game")
    flag = input()    
    return flag

# for start the game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nthis is ur turn",players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            position[p] = v
            print_board(position)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\n\nHurray !!,",players[0],"you win **")
                break
        else:
            print("\nthis is ur turn",players[1])
            p = int(input("Please Enter postion : "))
            v = '0'
            position[p] = v
            print_board(position)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\nHurray !!,",players[1],"you win **")    
                break
    else:
        print("\n\nGame is Tie")
        
# check for winner 
def checkwin(v):
    for i in winning_conditions:
        if (position[i[0]], position[i[1]], position[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (position[i[0]], position[i[1]], position[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner

# main code 
position = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = print_instructions()
if flag == 's' or flag == 'S':
    startgame()        
else:
    print("Invalid Entry")
