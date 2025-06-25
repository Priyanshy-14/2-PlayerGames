import cowsay
from pyfiglet import Figlet
import tkinter as tk
from tkinter import messagebox
import random


def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if "" not in board:
        return "Draw"
    return None

def decide_winner(p1, p2, vs_computer=False):
    if p1 == p2:
        return "Draw"
    elif (p1 == "Rock" and p2 == "Scissors") or \
         (p1 == "Paper" and p2 == "Rock") or \
         (p1 == "Scissors" and p2 == "Paper"):
        return "Player 1 wins!"
    else:
        return "Computer wins!" if vs_computer else "Player 2 wins!"
    

def format_score(score_a: int, score_b: int) -> str:
    return f"Player A: {score_a}    Player B: {score_b}"

def evaluate_guess(secret: int, guess: int) -> str:
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"


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
            print(f1.renderText("Thanks for Playing!"))
            cowsay.stegosaurus("GOOD BYEEE!!!")
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
        global board
        board = [""] * 9
        buttons = []


        def computer_move():
            empty_indices = [i for i, v in enumerate(board) if v == ""]
            if empty_indices:
                move = random.choice(empty_indices)
                board[move] = "O"
                buttons[move].config(text="O", state="disabled")
                winner = check_winner(board)
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
    def launch_game(vs_computer):
        mode_win.destroy()  # close mode window

        game = tk.Tk()
        game.title("Rock Paper Scissors")
        game.geometry("400x300")
        game.resizable(False, False)

        player_turn = [1]  # 1 or 2 for player switch
        player1_choice = [""]
        player2_choice = [""]


        def handle_choice(choice):
            if vs_computer:
                comp_choice = random.choice(["Rock", "Paper", "Scissors"])
                result = decide_winner(choice, comp_choice, vs_computer=True)  
                messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {comp_choice}\n\n{result}")
                reset_game()
            else:
                if player_turn[0] == 1:
                    player1_choice[0] = choice
                    label.config(text="Player 2, make your choice")
                    player_turn[0] = 2
                else:
                    player2_choice[0] = choice
                    result = decide_winner(player1_choice[0], player2_choice[0]) 
                    messagebox.showinfo("Result", f"Player 1 chose {player1_choice[0]}\nPlayer 2 chose {player2_choice[0]}\n\n{result}")
                    reset_game()

        def reset_game():
            player_turn[0] = 1
            player1_choice[0] = ""
            player2_choice[0] = ""
            label.config(text="Make your choice:")

        def exit_game():
            game.destroy()

        label = tk.Label(game, text="Make your choice:", font=("Arial", 16))
        label.pack(pady=20)

        btn_frame = tk.Frame(game)
        btn_frame.pack()

        for i, option in enumerate(["Rock", "Paper", "Scissors"]):
            tk.Button(btn_frame, text=option, font=("Arial", 14),
                      width=10, command=lambda opt=option: handle_choice(opt)).grid(row=0, column=i, padx=5)

        bottom_frame = tk.Frame(game)
        bottom_frame.pack(pady=20)

        tk.Button(bottom_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=10)
        tk.Button(bottom_frame, text="Exit", width=10, command=exit_game).grid(row=0, column=1, padx=10)

        game.mainloop()

    # Mode Selection Window
    mode_win = tk.Tk()
    mode_win.title("Choose Game Mode")
    mode_win.geometry("300x200")
    mode_win.resizable(False, False)

    tk.Label(mode_win, text="Play Rock Paper Scissors", font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(mode_win, text="Play with Friend", font=("Arial", 12), width=20,
              command=lambda: launch_game(False)).pack(pady=10)

    tk.Button(mode_win, text="Play with Computer", font=("Arial", 12), width=20,
              command=lambda: launch_game(True)).pack(pady=5)

    mode_win.mainloop()





def ping_pong():
    game = tk.Tk()
    game.title("Pong - 2 Player")
    game.resizable(False, False)
    game.geometry("700x500")

    canvas = tk.Canvas(game, bg="black", width=700, height=450)
    canvas.pack()

    # Created paddles and ball
    paddle_a = canvas.create_rectangle(20, 150, 40, 250, fill="white")
    paddle_b = canvas.create_rectangle(660, 150, 680, 250, fill="white")
    ball = canvas.create_oval(340, 210, 360, 230, fill="white")

    score_a = 0
    score_b = 0
    dx, dy = 4, 4  # Ball direction and speed

    score_text = canvas.create_text(350, 30, fill="white", font=("Arial", 20),
                                    text="Player A: 0    Player B: 0")

    def update_score():
        canvas.itemconfig(score_text, text=f"Player A: {score_a}    Player B: {score_b}")

    def move_paddle_a_up(event):
        canvas.move(paddle_a, 0, -20)

    def move_paddle_a_down(event):
        canvas.move(paddle_a, 0, 20)

    def move_paddle_b_up(event):
        canvas.move(paddle_b, 0, -20)

    def move_paddle_b_down(event):
        canvas.move(paddle_b, 0, 20)

    def reset_game():
        nonlocal score_a, score_b, dx, dy
        score_a = 0
        score_b = 0
        update_score()
        canvas.coords(ball, 340, 210, 360, 230)
        dx, dy = 4, 4

    def exit_game():
        game.destroy()

    def game_loop():
        nonlocal dx, dy, score_a, score_b

        canvas.move(ball, dx, dy)
        ball_coords = canvas.coords(ball)
        paddle_a_coords = canvas.coords(paddle_a)
        paddle_b_coords = canvas.coords(paddle_b)

        # Bounce on top/bottom
        if ball_coords[1] <= 0 or ball_coords[3] >= 450:
            dy = -dy

        # Bounce on paddles
        if (ball_coords[0] <= paddle_a_coords[2] and
            paddle_a_coords[1] < ball_coords[3] and
            paddle_a_coords[3] > ball_coords[1]):
            dx = abs(dx)

        if (ball_coords[2] >= paddle_b_coords[0] and
            paddle_b_coords[1] < ball_coords[3] and
            paddle_b_coords[3] > ball_coords[1]):
            dx = -abs(dx)

        # Score update
        if ball_coords[0] <= 0:
            score_b += 1
            update_score()
            canvas.coords(ball, 340, 210, 360, 230)
            dx = abs(dx)

        elif ball_coords[2] >= 700:
            score_a += 1
            update_score()
            canvas.coords(ball, 340, 210, 360, 230)
            dx = -abs(dx)

        game.after(30, game_loop)

    # Key bindings
    game.bind("w", move_paddle_a_up)
    game.bind("s", move_paddle_a_down)
    game.bind("<Up>", move_paddle_b_up)
    game.bind("<Down>", move_paddle_b_down)

    # Buttons
    control_frame = tk.Frame(game, bg="black")
    control_frame.pack(pady=5)

    tk.Button(control_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=10)
    tk.Button(control_frame, text="Exit", width=10, command=exit_game).grid(row=0, column=1, padx=10)

    game_loop()
    game.mainloop()





def guess_the_number():
    def start_game(vs_computer):
        select_window.destroy()  
        game = tk.Tk()
        game.title("Guess the Number")
        game.geometry("400x300")
        game.resizable(False, False)

        secret_number = [0]
        attempts = [0]

        if vs_computer:
            secret_number[0] = random.randint(1, 100)
            instructions = "Guess a number between 1 and 100"
        else:
            def set_number():
                try:
                    num = int(entry.get())
                    if not (1 <= num <= 100):
                        raise ValueError
                    secret_number[0] = num
                    entry.delete(0, tk.END)
                    label.config(text="Player 2, start guessing!")
                    entry.config(show="")
                    start_btn.config(text="Submit Guess", command=submit_guess)
                except ValueError:
                    messagebox.showerror("Error", "Enter a number between 1 and 100")
            instructions = "Player 1, enter a number (1–100)"
        label = tk.Label(game, text=instructions, font=("Arial", 14))
        label.pack(pady=20)

        entry = tk.Entry(game, font=("Arial", 14), width=10)
        entry.pack()

        result_label = tk.Label(game, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def submit_guess():
            try:
                guess = int(entry.get())
                attempts[0] += 1
                if guess < secret_number[0]:
                    result_label.config(text="Too low!")
                elif guess > secret_number[0]:
                    result_label.config(text="Too high!")
                else:
                    messagebox.showinfo("Correct!", f"You guessed it in {attempts[0]} attempts!")
                    reset_game()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
            entry.delete(0, tk.END)

        def reset_game():
            attempts[0] = 0
            result_label.config(text="")
            entry.delete(0, tk.END)
            if vs_computer:
                secret_number[0] = random.randint(1, 100)
                label.config(text="Guess a number between 1 and 100")
            else:
                label.config(text="Player 1, enter a number (1–100)")
                entry.config(show="*")
                start_btn.config(text="Set Number", command=set_number)

        def exit_game():
            game.destroy()

        if vs_computer:
            start_btn = tk.Button(game, text="Submit Guess", font=("Arial", 12), command=submit_guess)
        else:
            entry.config(show="*")
            start_btn = tk.Button(game, text="Set Number", font=("Arial", 12), command=set_number)

        start_btn.pack(pady=10)

        bottom = tk.Frame(game)
        bottom.pack(pady=20)

        tk.Button(bottom, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=10)
        tk.Button(bottom, text="Exit", width=10, command=exit_game).grid(row=0, column=1, padx=10)

        game.mainloop()

    # Initial mode selection window
    select_window = tk.Tk()
    select_window.title("Choose Game Mode")
    select_window.geometry("300x200")
    select_window.resizable(False, False)

    tk.Label(select_window, text="Guess The Number", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(select_window, text="Play with Computer", font=("Arial", 12), width=20,
              command=lambda: start_game(True)).pack(pady=10)

    tk.Button(select_window, text="Play with Friend", font=("Arial", 12), width=20,
              command=lambda: start_game(False)).pack(pady=5)

    select_window.mainloop()



if __name__ == "__main__":
    main()
