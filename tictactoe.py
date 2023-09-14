import random

 
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def main():
    counter = 0
    while counter < 9:
        if (counter % 2 == 0):
            userinput()
        else:
            opponent(counter)
            printboard()
        checkwin(counter)
        counter = counter + 1
    print("is tie")
    exit()        


def printboard():
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print("--+---+--")
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print("--+---+--")
    print(board[2][0], '|', board[2][1], '|', board[2][2])


def userinput():
    while True:
        row_ref = int(input("what row to place your piece? "))
        column_ref = int(input("what column to place your piece? "))
        if(row_ref > 0 and row_ref < 4 and column_ref > 0 and column_ref < 4
        and board[row_ref - 1][column_ref -1] == " "):
            break
 
    board[row_ref - 1][column_ref - 1] = "x"


def opponent(counter):
    count = 0
    reference = random.randint(1, 9 - counter)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                count = count + 1
            if count >= reference:
                board[i][j] = "o"
                return
    

def checkwin(counter):
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " "):
            if counter % 2 == 0:
                print("player won")
                printboard()
                exit()
            else:
                print("bot won")
                printboard()
                exit()
  
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " "):
            if counter % 2 == 0:
                print("player won")
                printboard()
                exit()
            else:
                print("bot won")
                printboard()
                exit()  
    
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " "):
        if counter % 2 == 0:
            print("player won")
            printboard()
            exit()
        else:
            print("bot won")
            printboard()
            exit()

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " "):
        if counter % 2 == 0:
            print("player won")
            printboard()
            exit()
        else:
            print("bot won")
            printboard()
            exit()


main()
