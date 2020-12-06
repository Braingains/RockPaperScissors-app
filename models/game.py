class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


def play_game(player_1_choice, player_2_choice):
    if player_1_choice == "rock" and player_2_choice == "scissors":
        return 'Rock beats Scissors, player 1 wins!'
        
    elif player_1_choice == "paper" and player_2_choice == "rock":
        return 'Paper beats Rock, player 1 wins!'
        
    elif player_1_choice == "scissors" and player_2_choice == "paper":
        return 'Scissors beats Paper, player 1 wins!'

    elif player_2_choice == "rock" and player_1_choice == "scissors":
        return 'Rock beats Scissors, player 2 wins'
        
    elif player_2_choice == "paper" and player_1_choice == "rock":
        return 'Paper beats Rock, player 2 wins'
        
    elif player_2_choice == "scissors" and player_1_choice == "paper":
        return 'Scissors beats Paper, player 2 wins'   
    
    elif player_1_choice == player_2_choice:
        return 'Draw game, try again!'

    else: return 'invalid input, input must be rock paper or scissors in lower-case'