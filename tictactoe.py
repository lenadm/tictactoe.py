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
        counter = counter + 1
        


def printboard():
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print("--+---+--")
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print("--+---+--")
    print(board[2][0], '|', board[2][1], '|', board[2][2])

def play(row_ref, column_ref):
        board[row_ref - 1][column_ref - 1] = "x"

def userinput():
    row_ref = int(input("what row would you like to place your piece? "))
    column_ref = int(input("what column would you like to place your piece? "))

    while row_ref not in range(3) and column_ref not in range(3) or board[row_ref - 1][column_ref -1] != " ":
        row_ref = int(input("what row would you like to place your piece? "))
        column_ref = int(input("what column would you like to place your piece? "))
 
    play(row_ref, column_ref)

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
    

main()
