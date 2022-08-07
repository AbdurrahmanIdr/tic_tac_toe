def board_gen():
    # generates tic-tac-toc board
    board = [["X" for _ in range(3)] for _ in range(3)]

    n = 1
    for r in range(3):
        for c in range(3):
            board[r][c] = n
            n += 1
    return board


def displaying_board(board):
    for a in range(3):
        for j in range(3):
            print('+', end="")
            for i in range(8):
                print("-", end="")
        print("+")
        for c in range(3):
            for j in range(3):
                print('|', end="")
                for i in range(8):
                    s = ' '
                    if c == 1 and i == 3 and a == 0 and j == 0:
                        s = board[0][0]
                    if c == 1 and i == 3 and a == 0 and j == 1:
                        s = board[0][1]
                    if c == 1 and i == 3 and a == 0 and j == 2:
                        s = board[0][2]
                    if c == 1 and i == 3 and a == 1 and j == 0:
                        s = board[1][0]
                    if c == 1 and i == 3 and a == 1 and j == 1:
                        s = board[1][1]
                    if c == 1 and i == 3 and a == 1 and j == 2:
                        s = board[1][2]
                    if c == 1 and i == 3 and a == 2 and j == 0:
                        s = board[2][0]
                    if c == 1 and i == 3 and a == 2 and j == 1:
                        s = board[2][1]
                    if c == 1 and i == 3 and a == 2 and j == 2:
                        s = board[2][2]
                    print(s, end="")
            print("|")
    for j in range(3):
        print('+', end="")
        for i in range(8):
            print("-", end="")
    print("+")


def user_input(board=None, ch=0, player='Comp'):
    if board is None:
        board = board_gen()
    if player == 'Comp':
        v = "X"
    else:
        v = "O"

    if ch == 0:
        board[1][1] = v
    elif ch == 1:
        board[0][0] = v
    elif ch == 2:
        board[0][1] = v
    elif ch == 3:
        board[0][2] = v
    elif ch == 4:
        board[1][0] = v
    elif ch == 5:
        board[1][1] = v
    elif ch == 6:
        board[1][2] = v
    elif ch == 7:
        board[2][0] = v
    elif ch == 8:
        board[2][1] = v
    elif ch == 9:
        board[2][2] = v

    displaying_board(board)
    return board


def win_checker(win, used_box):
    if used_box[0] == win and used_box[1] == win and used_box[2] == win:
        return True

    elif used_box[3] == win and used_box[4] == win and used_box[5] == win:
        return True

    elif used_box[6] == win and used_box[7] == win and used_box[8] == win:
        return True

    elif used_box[0] == win and used_box[3] == win and used_box[6] == win:
        return True

    elif used_box[1] == win and used_box[4] == win and used_box[7] == win:
        return True

    elif used_box[2] == win and used_box[5] == win and used_box[8] == win:
        return True

    elif used_box[0] == win and used_box[4] == win and used_box[8] == win:
        return True

    elif used_box[2] == win and used_box[4] == win and used_box[6] == win:
        return True

    else:
        return False


def game():
    import random
    used_box = [1, 2, 3, 4, 'X', 6, 7, 8, 9]
    no_of_box_remains = 8
    board = user_input()
    next_player = 'User'
    final_check_mate = False
    while no_of_box_remains != 0:
        if next_player == 'Comp':
            comp = random.randrange(1, 10)
            if comp not in used_box and 0 < comp <= 9 or 0 >= comp > 9 or comp <= 0 or comp > 9:
                continue

            print("Computer entered: ", comp)
            board = user_input(board, comp, next_player)
            ind = used_box.index(comp)
            used_box[ind] = 'X'

            if win_checker('X', used_box):
                print("Computer wins")
                final_check_mate = True
                break

            next_player = 'User'
            no_of_box_remains -= 1

        else:
            value = input("Please select a box: ")

            if len(value) > 1 or value == '' or 48 < ord(value) > 57 or int(value) not in used_box:
                continue

            value = int(value)

            print("User entered: ", value)
            board = user_input(board, value, next_player)
            ind = used_box.index(value)
            used_box[ind] = 'O'

            if win_checker('O', used_box):
                print("User wins")
                final_check_mate = True
                break

            next_player = 'Comp'
            no_of_box_remains -= 1

    return final_check_mate


def start_game():
    s_game = game()
    while not s_game:
        play = input("Draw, Do you want to try again? Y or N: ")
        if play == 'Y' or 'yes' or 'Yes' or 'y':
            game()
        elif play == 'N' or 'n' or 'NO' or 'no' or 'No' or 'nO':
            break


start_game()
