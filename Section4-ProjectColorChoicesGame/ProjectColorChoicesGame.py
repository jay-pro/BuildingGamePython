#import random module
import random

#print multiline instruction
#performstring concatenation of string
print ("Wining Rules of the Color Choices Game as follows: "+"\Enter a number from one two five and match computer choice to Wi")
computer_score = 0
player_score = 0

while True:
    print ("red = 1\nyellow = 2\norange = 3\ngreen = 4\nblue = 5\ntake a turn: ")

    #take the input from user
    player_choice = int(input("User turn: "))

    #OR is the short-circuit operator
    #if any one of the condition is true
    #then it return True value

    #looping until user enter invalid input
    while player_choice > 5 and player_choice < 1:
        player_choice = int(input("enter valid input: "))

    #initialize value of choice_col variable
    #corresponding to the player_choice value
    if player_choice ==1:
        choice_col = 'red'
    elif player_choice == 2:
        choice_col = 'yellow'
    elif player_choice == 3:
        choice_col = 'orange'
    elif player_choice == 4:
        choice_col = 'green'
    else:
        choice_col = 'blue'

    #print user choice
    print("user color choice is: " + choice_col)
    print("\nNow its computer tủn to choose a color......")

    #computer chooses randomly any number
    #among 1,2 and 3. Using randint method
    #of random module
    computer_choice = random.randint(1,5)

    #looping until computer_choice value
    #is equal to the choice value
    while computer_choice == player_choice:
        computer_choice == random.randint(1,5)
    
    #initialize value of computer_choice_col
    #variable corresponding to the computer_choice value
    if computer_choice == 1:
        compu_choice_col = 'red'
    elif computer_choice == 2:
        compu_choice_col = 'yelow'
    elif computer_choice == 3:
        compu_choice_col = 'orange'
    elif computer_choice == 4:
        compu_choice_col = 'green'
    else:
        compu_choice_col = 'blue'

    print("Computer color choice is: "+ compu_choice_col)

    #conditions for wining
    if(choice_col == compu_choice_col):
        player_score += 1
        print("player_score: "+str(player_score))
        print("computer_score: "+str(computer_score))
    else:
        computer_score += 1

        print("player_score: "+str(player_score))
        print("computer_score: "+str(computer_score))

    #after coming out of the while loop
    #we print thanks for playing and the overal result of the Game
    if computer_score == player_score:
        print("Game is Tied\nThanks for playing")
    elif computer_score < player_score:
        print("Player is Victorious\n<<===User wins===>>\nThanks for playing")
    elif computer_score > player_score:
        print("<<===Computer wins===>>\nPlayer is Defeated\nThanks for playing")

    print("Do you want to play again? (Y/N): ")
    answer = input()

    #if user input n or N then codition is true

    if answer == "n" or answer == "N":
        break
