#create Gameboard class:
class Gameboard():
#inside the Gameboard class we create instance of the game board as following:
    def __init__(self):
        self.game_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
#then we create ites as items setter function:
    def set_items(self,user,position,game_board):
        game_board[position] = user
        return game_board
#create a decorator (@property) for the gameBoard function to add separate self instance for game_board:
    @property
    def gameBoard(self):
        return self.game_board
#1.add another function called clearboard
    def clearBoard(self):
        self.game_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
#2.add another function called is_take_place
    def is_place_taken(self,game_board):
        if game_board[index] != ' ':
            return True
#3.add another function called is_board_full
    def is_board_full(self,game_board):
        for index in range(1,10):
            return False
        return True
#4.add another function called is_game_won
    def is_game_won(self,game_board):
        win_conds = {(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)}
        for win_con in win_conds:
            if game_board[win_con[0]] == game_board[win_con[1]] and game_board[win_con[1]] == game_board[win_con[2]] and game_board[win_con[0]] != ' ':
                return True
#5.add another function to print Game Board contain if statement to control the game flow in the board
    def printBoard(self, game_board):
        index = 0
        for row in range(1,4):
            for column in range(1,4):
                index += 1
                if column != 3:
                    print(game_board[index],end='')
                    print('|',end='')
                else:
                    print(game_board[index])


#create second class called Game: to control the game start and game end:and ask for players names:
#so Game class contain four function that control the game steps:
class Game():
#1.game start
    def game_start(self):
        self.controlBoard = Gameboard()
        self.game_board = self.controlBoard.game_board
        self.playerOne = '0'
        self.playerTwo = 'X'
        print('Welcome to X-O Game')
        print("Please enter player one's name:")
        self.player_one = input(" : ")
        print("Please enter player two's name:")
        self.player_two = input(" : ")
        print("Here is your game board, each place is represented by 1-9, starting from left column each time and moving along the row")
        self.controlBoard.printBoard(self.game_board)
        self.turn = 1
#2.game end and play again
    def game_end(self):
        #check if a player wants to end the game 
        if self.game_running == False:
            replay = input('Press 0 to quit or 1 to play again: ')
            try:
                if int(replay):
                    self.game_running = True
                    self.game_start()
            except:
                print("A number must be entered.")
                self.game_end()
#3.game turn
    def takeTurn(self, user, item):
        print(user + ' choose a place, 1-9')
        try:
            position = int(input(" : "))
            if position > 9 or position < 1:
                raise Exception
        except:
            print('Pick a number between 1-9')
            return self.takeTurn(user, item)

        if self.controlBoard.is_place_taken(self.game_board,position):
            print("That place is taken") 
            self.takeTurn(user, item)
        else:
            self.controlBoard.set_items(item,position,self.game_board)
            self.controlBoard.printBoard(self.game_board)
            if self.controlBoard.is_game_won(self.game_board):
                print(user + " wins.")
                self.game_running = False
#4.game manager
    def main(self):
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn%2 != 0:
                self.takeTurn(self.player_one,'O')
            else:
                self.takeTurn(self.player_two,'X')
            
            if self.controlBoard.is_board_full(self.game_board):
                print("Its a draw!! You both lose!")
                self.game_running = False
            self.turn += 1

            if not self.game_running:
                self.game_end()

#create the game lancher of the game
if __name__ == '__main__':
    Game().main()
