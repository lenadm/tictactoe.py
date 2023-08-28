
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

    if row_ref not in range(3) and column_ref not in range(3):
        row_ref = int(input("what row would you like to place your piece? "))
        column_ref = int(input("what column would you like to place your piece? ")) 
    
    if(board[row_ref - 1][column_ref - 1] != " "):
        print("invalid only select an empty space")
        row_ref = int(input("what row would you like to place your piece? "))
        column_ref = int(input("what column would you like to place your piece? ")) 

    play(row_ref, column_ref)

main()
