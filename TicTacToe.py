'''Tic Tac Toe Milestone Project 1'''

'''
A board of nested lists, referenced by A-C, 1-3 grid positions
which will store 'X' and 'O' for player moves and an underscore
represents an unoccupied position.
'''

# Intro to game & example for userability
print ("-- Tic Tac Toe --\n")
print ("Input the row, them column of the space you would like to take!")
print ("For example, type A1 to take the top left hand corner,\nor C3 to take the bottom right corner.")

# Values for counts & storing taken grid positions
Play_Count = 0
Taken_Val = []
Taken_Total = " "

       
'''Creating the grid'''

grid = []
for (x) in range(0,3):  # function to create a 3 x 3 grid
    grid.append(["_"]*3)
   
def print_grid(grid):  # function to print the grid with rows labelled A, B, C
    ABC = "ABC"
    row = 0
    for (num) in grid:  # for each row (list) in grid - label and join with pipe
         print (((ABC)[(row)])+": |"+"|".join(num))
         row += 1


'''Play function'''

def play():
    global Taken_Total
    Play = input("\n\nWhere on the grid would you like to place your marker?: ").lower()
    
    # Validating input
    while True:
        if len(Play) != 2:
            Play = input ("Invalid Input. Please try again: ").lower()
        elif ((Play)[0]) not in ("abc"):
            Play = input ("Invalid Input. Please try again: ").lower()
        elif ((Play)[1]) not in ("123"):
            Play = input ("Invalid Input. Please try again: ").lower()
        elif (Play) in (Taken_Val):
            Play = input ("Invalid Input. Please try again: ").lower()
        else:
            break
       
    # Storing move
    Taken_Val.append(Play)
    Taken_Total += ((Play)+(Player))
    
    # Changing Grid - adding marker
    while True:
        if (Play) == "a1" and grid[0][0] == "_":
            grid[0][0] = (Player)
            break
        elif (Play) == "a2" and grid[0][1] == "_":
            grid[0][1] = (Player)
            break
        elif (Play) == "a3" and grid[0][2] == "_":
            grid[0][2] = (Player)
            break
        elif (Play) == "b1" and grid[1][0] == "_":
            grid[1][0] = (Player)
            break
        elif (Play) == "b2" and grid[1][1] == "_":
            grid[1][1] = (Player)
            break
        elif (Play) == "b3" and grid[1][2] == "_":
            grid[1][2] = (Player)
            break
        elif (Play) == "c1" and grid[2][0] == "_":
            grid[2][0] = (Player)
            break
        elif (Play) == "c2" and grid[2][1] == "_":
            grid[2][1] = (Player)
            break
        elif (Play) == "c3" and grid[2][2] == "_":
            grid[2][2] = (Player) 
            break

## Winning Combinations - Taken_Val
while True:
    # A across - O
    if ("a1O") in (Taken_Total) and("a2O") in (Taken_Total) and("a3O") in (Taken_Total):
        break
    # A across - X
    if ("a1X") in (Taken_Total) and ("a2X") in (Taken_Total) and ("a3X") in (Taken_Total):
        break
    # B across - O
    if ("b1O") in (Taken_Total) and ("b2O") in (Taken_Total) and ("b3O") in (Taken_Total):
        break
    # B across - X
    if ("b1X") in (Taken_Total) and ("b2X") in (Taken_Total) and("b3X") in (Taken_Total):
        break
    # C across - O
    if ("c1O") in (Taken_Total) and ("c2O") in (Taken_Total) and("c3O") in (Taken_Total):
        break
    # C across - X
    if ("c1X") in (Taken_Total) and ("c2X") in (Taken_Total) and("c3X") in (Taken_Total):
        break
    # 1st Col Down - O
    if ("a1O") in (Taken_Total) and ("b1O") in (Taken_Total) and ("c1O") in (Taken_Total):
        break
    # 1st Col Down - X
    if ("a1X") in (Taken_Total) and ("b1X") in (Taken_Total) and ("c1X") in (Taken_Total):
        break
    # 2nd Col Down - O
    if ("a2O") in (Taken_Total) and ("b2O") in (Taken_Total) and("c2O") in (Taken_Total):
        break
    # 2nd Col Down - X
    if ("a2X") in (Taken_Total) and ("b2X") in (Taken_Total) and ("c2X") in (Taken_Total):
        break
    # 2rd Col Down - O
    if ("a3O") in (Taken_Total) and ("b3O") in (Taken_Total) and("c3O") in (Taken_Total):
        break
    # 3rd Col Down - X
    if ("a3X") in (Taken_Total) and ("b3X") in (Taken_Total) and ("c3X") in (Taken_Total):
        break
    # Diagonally Left to Right - O
    if ("a1O") in (Taken_Total) and ("b2O") in (Taken_Total) and ("c3O") in (Taken_Total):
        break
    # Diagonally Left to Right - X
    if ("a1X") in (Taken_Total) and ("b2X") in (Taken_Total) and ("c3X") in (Taken_Total):
        break
    # Diagonally Right to Left - O
    if ("a3O") in (Taken_Total) and ("b2O") in (Taken_Total) and ("c1O") in (Taken_Total):
        break
    # Diagonally Right to Left - X
    if ("a3X") in (Taken_Total) and ("b2X") in (Taken_Total) and ("c1X") in (Taken_Total):
        break
       
    else:
        
        print("\n")  # phew! The main code function
       
        '''Play Count - Switches Players & keeps track in case of draw'''
        (Play_Count) += 1
        if (Play_Count) == 10:  # checking for draw
            print("\n-- It's a draw! Everyone loses! --")
            print("\nFinal Grid:")
            break
        # Switching players
        if (Play_Count)%2==0:
            Player = "X"
        else:
            Player = "O"
        print ((Player),"'s Turn!\n")
        print_grid(grid)
        play()

print("\n")
print_grid(grid)
        
# Winner!
if Play_Count != 10:  # printing winning result
    print ("\n\n-- Game Over --")
    print ("-- ",(Player)," is the winner! --")
print("\nThanks for playing!\n")
