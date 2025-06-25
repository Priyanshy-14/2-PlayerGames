import pytest
from project import check_winner
from project import decide_winner

def test_x_wins_row():
    board = ["X", "X", "X",
             "", "", "",
             "", "", ""]
    assert check_winner(board) == "X"

def test_o_wins_column():
    board = ["O", "", "",
             "O", "", "",
             "O", "", ""]
    assert check_winner(board) == "O"

def test_x_wins_diagonal():
    board = ["X", "", "",
             "", "X", "",
             "", "", "X"]
    assert check_winner(board) == "X"

def test_draw():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "X"]
    assert check_winner(board) == "Draw"

def test_incomplete_game():
    board = ["X", "O", "X",
             "X", "", "O",
             "", "X", "O"]
    assert check_winner(board) == None



def test_draw():
    assert decide_winner("Rock", "Rock") == "Draw"
    assert decide_winner("Paper", "Paper") == "Draw"
    assert decide_winner("Scissors", "Scissors") == "Draw"

def test_player1_wins():
    assert decide_winner("Rock", "Scissors") == "Player 1 wins!"
    assert decide_winner("Paper", "Rock") == "Player 1 wins!"
    assert decide_winner("Scissors", "Paper") == "Player 1 wins!"

def test_player2_wins():
    assert decide_winner("Rock", "Paper") == "Player 2 wins!"
    assert decide_winner("Paper", "Scissors") == "Player 2 wins!"
    assert decide_winner("Scissors", "Rock") == "Player 2 wins!"

def test_vs_computer():
    assert decide_winner("Rock", "Paper", vs_computer=True) == "Computer wins!"
    assert decide_winner("Scissors", "Paper", vs_computer=True) == "Player 1 wins!"