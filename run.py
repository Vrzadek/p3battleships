import random
import os


# constants that set the grid size
ROWS = 5
COLUMNS = 5


def main_menu():
    instructions()
    setup()


# some info for the user
def instructions():
        print("Welcome to Battleships!")
        print("There's 3 hidden ships. You have 10 rounds. You get 1 bonus round if you hit a ship. :)")
        input("Press any key to continue:")
        os.system('cls')


# creates the game board, sets the numbers for ships + rounds and creates a list with ship coordinates
def setup():
    game_board = [[0] * COLUMNS for _ in range(ROWS)]

    ships_left = 3 
    rounds_left = 10

    ship_coordinates = []
    for _ in range(ships_left):
        ship_coordinates.append(create_ship())

    play_game(game_board, ship_coordinates, ships_left, rounds_left) # these are then all sent to the play_game() function


# creates ship coordinates
def create_ship():
    return random.randrange(ROWS), random.randrange(COLUMNS)


#prints the grid
def print_board(game_board):
    for i in game_board:
        print(*i)
    print("") #just for new line


# all the game logic is in this function and uses data from the setup() function
def play_game(game_board, ship_coordinates, ships_left, rounds_left):
    print_board(game_board)
 
    print(f"Rounds left: {rounds_left} | Ships left: {ships_left}")
    #print(ship_coordinates) # this can be usueful for testing aka cheat to see where the ships are
   
    while rounds_left > 0 and ships_left > 0: # as long as we have rounds or ships left, we ask user for input

        row_input_ok = False
        col_input_ok = False
        
        # these 2 while-loops check that the input is only numbers and in the accepted range
        while (row_input_ok == False):
            try:
                row = int(input(f"Enter a row number between 1-{ROWS} >: "))
            except ValueError:
                print("Only numbers please :)")
                continue
            if row not in range(1,ROWS+1):
                print(f"The number must be between 1-{ROWS}!")
                continue
            row_input_ok = True

        row -= 1 # adjusting the number for 0-based indexing    
            
        while (col_input_ok == False):
            try:
                column = int(input(f"Enter a column number between 1-{COLUMNS} >: "))
            except ValueError:
                print("Only numbers please :)")
                continue
            if column not in range(1,COLUMNS+1):
                print(f"The number must be between 1-{COLUMNS}!")
                continue
            col_input_ok = True

        column -= 1 # adjusting the number for 0-based indexing   

        if game_board[row][column] == "-" or game_board[row][column] == "X": # checks if we've already marked that coordinate
            print("\nYou've already tried that spot!\n")
            continue
        elif (row, column) in ship_coordinates: # checks if the guessed coordinates is one of the 3 in the ship_coordinates list - if yes marks that coordinate with an "X"
            os.system('cls')
            print("Wow you got it! Good job! You were granted a bonus round! :D\n")
            game_board[row][column] = "X"
            ships_left -= 1 # reduces the ship counter
            print_board(game_board)
            print(f"Rounds left: {rounds_left} | Ships left: {ships_left}")
            if ships_left == 0: # checks for the win condition (zero ships left)
                os.system('cls')
                print("Wow you got them all! You WIN! :D\n")
                game_board[row][column] = "X"
                print_board(game_board)
                play_again()
        else:
            os.system('cls')
            print("You missed! :(\n")
            game_board[row][column] = "-" # if not in the ship_coordinates list - marks that coordinate with an "-"
            rounds_left -= 1
            print_board(game_board)
            print(f"Rounds left: {rounds_left} | Ships left: {ships_left}")
            if rounds_left == 0: # checks for the lose condition (zero rounds left)
                os.system('cls')
                print("Sorry, you're out of rounds. You lose. :(\n")
                game_board[row][column] = "-"
                print_board(game_board)
                play_again()


# this gets called upon winning or losing    
def play_again():
    try_again = input("Wanna play again? (Y)es or (N)o? >: ").lower()
    if try_again == "y":
        os.system('cls')
        print("Here we go again! Good luck! :D\n")
        setup() # returns to setup() where new ship coordinates are created and rounds+ship counters are reset
    else:
        os.system('cls')
        print("Goodbye! :')")
        return   


if __name__ == "__main__":
    main_menu()
