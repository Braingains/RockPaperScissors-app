import unittest

from models.game import Game, play_game
from models.player import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.Rocky = Player('Rocky', 'rock')
        self.Sissy = Player('Sissy', "scissors")
        self.Pepe = Player('Pepe', 'paper')

    def test_player_has_name(self):
        self.assertEqual('Rocky', self.Rocky.name)

    def test_player_has_choice(self):
        self.assertEqual('rock', self.Rocky.choice)

    def test_rock_beats_scissors(self):
        self.assertEqual(play_game(self.Rocky.choice, self.Sissy.choice), 'Rock beats Scissors, player 1 wins!')

    def test_scissors_beats_paper(self):
        self.assertEqual(play_game(self.Sissy.choice, self.Pepe.choice), 'Scissors beats Paper, player 1 wins!')

    def test_paper_beats_rock(self):
        self.assertEqual(play_game(self.Rocky.choice, self.Pepe.choice), 'Paper beats Rock, player 2 wins')

    def test_draw(self):
        self.assertEqual(play_game(self.Rocky.choice, self.Rocky.choice), 'Draw game, try again!')

    def test_invalid(self):
        self.assertEqual(play_game('spoon', 'fork'), 'invalid input, input must be rock paper or scissors in lower-case')