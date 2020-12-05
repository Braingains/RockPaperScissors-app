class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


def play_game(player_1_choice, player_2_choice):
    if player_1_choice == "Rock" and player_2_choice == "Scissors":
        return 'Rock'
        
    if player_1_choice == "Paper" and player_2_choice == "Rock":
        return 'Paper'
        
    if player_1_choice == "Scissors" and player_2_choice == "Paper":
        return 'Scissors'

    if player_2_choice == "Rock" and player_1_choice == "Scissors":
        return 'Rock'
        
    if player_2_choice == "Paper" and player_1_choice == "Rock":
        return 'Paper'
        
    if player_2_choice == "Scissors" and player_1_choice == "Paper":
        return 'Scissors'   
    
    else: return 'Draw'