from random import randint


# -----------------------------------------
# Functions
# -----------------------------------------

def random_row(len_rows):
    return randint(0, len_rows - 1)


def random_col(len_cols):
    return randint(0, len_cols - 1)


def get_random_ships(n_ships, board):
    len_cols = len(board[0])
    len_rows = len(board)

    l_ships = {}

    for n in range(n_ships):
        l_ships[n] = [random_row(len_rows), random_col(len_cols)]

    return l_ships


def print_board(board):
    for row in board:
        print(" ".join(row))


def check_atack(g_row, g_col, m_ships, battlefild_size, board):
    success = -1
    if g_row < 0 or g_row >= battlefild_size:
        print("Oops, that's not even in the ocean. Row is out of bound!")
    elif g_col < 0 or g_col >= battlefild_size:
        print("Oops, that's not even in the ocean. Column is out of bound!")
    elif board[g_row][g_col] == "X" or board[g_row][g_col] == "+":
        print("You guessed that one already.")
    else:
        for ship in m_ships:
            if m_ships[ship][0] == g_row and m_ships[ship][1] == g_col:
                print("Congratulations! You sunk my battleship!")
                success = 1
                break
        if success != 1:
            print("You missed my battleship!")
            success = 0
    return success


def update_chance(success, chance, max_chance):
    switcher = {
        0: 1,
        1: -1
    }
    chance -= switcher[success]
    if chance < 0:
        chance = 0
    elif chance > max_chance:
        chance = max_chance
    return chance


def update_board(g_row, g_col, success, board):
    switcher = {
        0: 'X',
        1: '+'
    }
    board[g_row][g_col] = switcher[success]
    return board


# -----------------------------------------
# Main
# -----------------------------------------

# variables

battlefieldSize = 5
ships = 4
maxChance = 4

chance = maxChance
turn = 1

print("Lets play battleship!")

board = []

for x in range(battlefieldSize):
    board.append(["O"] * battlefieldSize)

machine_ships = get_random_ships(ships, board)

print(machine_ships)

while chance >= 0:
    if chance > 0:
        print_board(board)
        print("Turn: ", turn)
        print("Chances", chance)

        guess_row = input("Guess Row:")
        guess_col = input("Guess Col:")

        if guess_col != "" and guess_row != "":
            guess_row = int(guess_row)
            guess_col = int(guess_col)
            success = check_atack(guess_row, guess_col, machine_ships, battlefieldSize, board)

            if success != -1:
                turn += 1
                chance = update_chance(success, chance, maxChance)
                board = update_board(guess_row, guess_col, success, board)
    else:
        print("--------------------\nGame Over\n--------------------")
        break
