from random import randint 

#-----------------------------------------
#	Functions
#-----------------------------------------
        
def random_row(len_rows):
    return randint(0, len_rows - 1)

def random_col(len_cols):
    return randint(0, len_cols - 1)

def getRandomShips(n_ships, board):
	len_cols = len(board[0])
	len_rows = len(board)
	
	l_ships = {}

	for n in range(n_ships):
		l_ships[n] = [random_row(len_rows), random_col(len_cols)]

	return l_ships

def print_board(board):
	for row in board:
		print " ".join(row)

def checkAtack(g_row, g_col, machine_ships, battlefildSize, board):
	success = -1
	if (g_row < 0 or g_row >= battlefildSize):
		print("Oops, that's not even in the ocean. Row is out of bound!")
	elif (g_col < 0 or g_col >= battlefildSize):
		print("Oops, that's not even in the ocean. Column is out of bound!")
	elif (board[g_row][g_col] == "X" or board[g_row][g_col] == "+"):
		print("You guessed that one already.")
	else:
		for ship in machine_ships:
			if machine_ships[ship][0] == g_row and machine_ships[ship][1] == g_col:
				print("Congratulations! You sunk my battleship!")
				success = 1
				break
		if success != 1:
			print("You missed my battleship!")
			success = 0
	return success

def updateChance(success, chance, maxChance):
	switcher = {
		0 : 1,
		1 : -1
	}

	print switcher[success]
	chance -= switcher[success]
	if chance < 0:
		chance = 0
	elif chance > maxChance:
		chance = maxChance
	print "chances", chance
	return chance



def updateBoard(guess_row, guess_col, success, board):
	switcher = {
		0 : 'X',
		1 : '+'
	}

	board[guess_row][guess_col] = switcher[success]

	return board



#-----------------------------------------
#	Main
#-----------------------------------------

#---- variables

battlefildSize = 5
ships = 4
maxChance = 4

chance = maxChance
turn = 1

print "Lets play battleship!"

board = []

for x in range(battlefildSize):
    board.append(["O"] * battlefildSize)

machine_ships =  getRandomShips(ships, board)

print machine_ships


while (chance >= 0):
	if chance > 0:
		print_board(board)
		print "Turn: ", turn

		guess_row = int(raw_input("Guess Row:"))
		guess_col = int(raw_input("Guess Col:"))

		if(guess_col != "" and guess_row != ""):
			success = checkAtack(guess_row, guess_col, machine_ships, battlefildSize, board)

			if success != -1:
				turn += 1
				chance = updateChance(success, chance, maxChance)
				board = updateBoard(guess_row, guess_col, success, board)
	else:
		print "Game Over"
		break