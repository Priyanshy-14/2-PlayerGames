import cowsay
from pyfiglet import Figlet
import tkinter as tk
from tkinter import messagebox
import random
#from tabulate import tabulate

def main():
    x = "2-Player Games"
    f = Figlet(font = "slant")
    f1 = Figlet(font = "serifcap")
    print(f.renderText(x))

    while True:
        print("================================")
        print("Select a Game of Your Choice")
        print("================================")
        print("1. Tic Tac Toe")
        print("2. Rock Paper Scissors")
        print("3. Ping Pong")
        print("4. Guess the Number")
        print("5. __EXIT__")

        choice = input("Select a game (1-5): ")

        if choice =="1":
            tic_tac_toe()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            ping_pong()
        elif choice == "4":
            guess_the_number()
        elif choice == "5":
            cowsay.stegosaurus("Thanks for Playing!")
            break
        else: 
            print("Invalid Choice. Try Again!")



def tic_tac_toe():
    def launch_game(vs_computer):
        # Close the mode selection window
        select_win.destroy()

        # New game window
        game = tk.Tk()
        game.title("Tic Tac Toe")
        game.geometry("300x350")
        game.resizable(False, False)

        current_player = ["X"]
        board = [""] * 9
        buttons = []

        def check_winner():
            wins = [(0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6)]
            for i, j, k in wins:
                if board[i] == board[j] == board[k] and board[i] != "":
                    return board[i]
            if "" not in board:
                return "Draw"
            return None

        def computer_move():
            empty_indices = [i for i, v in enumerate(board) if v == ""]
            if empty_indices:
                move = random.choice(empty_indices)
                board[move] = "O"
                buttons[move].config(text="O", state="disabled")
                winner = check_winner()
                if winner:
                    show_result(winner)

        def show_result(winner):
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a Draw!")
            else:
                messagebox.showinfo("Winner", f"Player {winner} wins!")
            reset_board()

        def on_click(i):
            if board[i] == "":
                board[i] = current_player[0]
                buttons[i].config(text=current_player[0], state="disabled")
                winner = check_winner()
                if winner:
                    show_result(winner)
                    return
                if vs_computer:
                    computer_move()

        def reset_board():
            for i in range(9):
                board[i] = ""
                buttons[i].config(text="", state="normal")
            current_player[0] = "X"

        def exit_game():
            game.destroy()

        tk.Label(game, text="Tic Tac Toe", font=("Arial", 18, "bold")).pack(pady=10)

        frame = tk.Frame(game)
        frame.pack()

        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 16), width=5, height=2,
                            command=lambda i=i: on_click(i))
            btn.grid(row=i//3, column=i%3)
            buttons.append(btn)

        bottom_frame = tk.Frame(game)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text="Reset", command=reset_board, width=10).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text="Exit", command=exit_game, width=10).grid(row=0, column=1, padx=5)

        game.mainloop()

    # Initial mode selection window
    select_win = tk.Tk()
    select_win.title("Choose Game Mode")
    select_win.geometry("300x200")
    select_win.resizable(False, False)

    tk.Label(select_win, text="Choose Game Mode", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(select_win, text="Play with Friend", font=("Arial", 12), width=20,
              command=lambda: launch_game(False)).pack(pady=10)

    tk.Button(select_win, text="Play with Computer", font=("Arial", 12), width=20,
              command=lambda: launch_game(True)).pack(pady=5)

    select_win.mainloop()

def rock_paper_scissors():
    ...

def ping_pong():
    ...

def guess_the_number():
    ...



if __name__ == "__main__":
    main()
