class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


def play_game(player_1_choice, player_2_choice):
    
    winner = "Player_2"

    if player_1_choice == "rock" and player_2_choice == "scissors":
        winner = "Player_1"
    if player_1_choice == "scissors" and player_2_choice == "paper":
        winner = "Player_1"
    if player_1_choice == "paper" and player_2_choice == "rock":
        winner = "Player_1"
    if player_1_choice == player_2_choice:
        winner = "Tie"
    

    return winner

    #else: return 'invalid input'