import cowsay
from pyfiglet import Figlet
#from tabulate import tabulate

def main():
    x = "2-Player Games"
    f = Figlet(font = "slant")
    print(f.renderText(x))

    while True:
        print("--------------------")
        print("Select a Game of Your Choice")
        print("--------------------")
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
            print(f.renderText("Thanks for playing")) 
            break
        else: 
            print("Invalid Choice. Try Again!")



def tic_tac_toe():
    ...


def rock_paper_scissors():
    ...

def ping_pong():
    ...

def guess_the_number():
    ...



if __name__ == "__main__":
    main()
