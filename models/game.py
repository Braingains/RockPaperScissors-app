import random
class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


#these function should be returning the winning player object, rather than just a string

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

def cpu_choice():
    choices = ['rock', 'paper', 'scissors']
    return choices[random.randint(0, 2)]

def play_cpu(player_1_choice, computer_choice):

    winner = "computer"

    if player_1_choice == "rock" and computer_choice == "scissors":
        winner = "Player_1"
    if player_1_choice == "scissors" and computer_choice == "paper":
        winner = "Player_1"
    if player_1_choice == "paper" and computer_choice == "rock":
        winner = "Player_1"
    if player_1_choice == computer_choice:
        winner = "Tie"
    

    return winner