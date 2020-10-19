while 1:
    m0 = "@"
    n_ = " "
    board_size = int(input("enter the size of the board..."))
    print("\n\n\n\n")
    for q in range(4):
        for z in range(board_size//2):
            for j in range(4):  # printing with gapes to make 8 grids
                for a in range(board_size):
                    print(m0, end='')  # printing zero
                for a in range(board_size):
                    print(n_, end='')  # printing space
            print('')
        for z in range(board_size//2):
            for j in range(4):  # printing with gapes to make 8 grids
                for a in range(board_size):
                    print(n_, end='')  # printing zero
                for a in range(board_size):
                    print(m0, end='')  # printing space
            print('')
