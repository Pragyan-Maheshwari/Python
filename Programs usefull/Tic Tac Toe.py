board = [[0,0,0],[0,0,0],[0,0,0]]
turns = [1,2,3,4,5,6,7,8,9]
for i in turns:
    if i%2 == 1:
        print("")
        print("'X's turn")
        cellValue = 1
    elif i%2 == 0:
        print("'O's turn")
        cellValue =-1
    print(f"{board[0]}\n{board[1]}\n{board[2]}")
    r,c = input("Please enter the row and collum where u want to play: ")
    r = int(r)
    c = int(c)
    while board[r][c] != 0:
        print("This place has already been filled.")
        r,c = input("Please enter the row and collum where u want to play: ")
        r = int(r)
        c = int(c)
    if board[r][c] == 0:
        board[r][c] = cellValue
    # Checking Winner
    h = 0
    if i >= 5:
        while h <= 2:
            r = 0 ; c = 0 ; check = 0 ; sumt = 0 ; sun = 0
            while check <= 2:
                sumt = sum(board[r])
                if sumt == 3:
                    print("X won")
                    quit()
                elif sumt == -3:
                    print("O won")
                    quit()
                sun = sun + board[r][c]
                if sun ==3:
                    print("X won")
                    quit()
                elif sun == -3:
                    print("O won")
                    quit()
                c = c+1 ; check = check + 1

        if board[0][2]+board[1][1]+board[2][0] == 3:
            print("X won")
            quit()
        elif board[0][2]+board[1][1]+board[2][0] == -3:
            print("O won")
            quit()
        if board[0][0]+board[1][1]+board[2][2] == 3:
            print("X won")
            quit()
        elif board[0][0]+board[1][1]+board[2][2] == -3:
            print("O won")
            quit()