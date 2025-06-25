# 2-Player Games Arcade

#### Description:

Welcome to **2-Player Games Arcade** — a fun, interactive terminal-based and GUI-powered mini-game suite written entirely in Python! This final project for CS50P brings together four classic games, each designed to be played either with a friend or against the computer, showcasing both real-time user interaction and game logic.

Upon running the project, users are greeted with a terminal menu where they can choose from the following games:

1. **Tic Tac Toe**
2. **Rock Paper Scissors**
3. **Pong (Ping-Pong 2 Player Game)**
4. **Guess the Number**
5. **Exit**

Each game opens in a separate Tkinter window with a clean and responsive GUI, and includes options to play with a friend or against an AI opponent (where applicable). Users can reset or exit each game using buttons, and are returned to the main menu upon completion.

---

### Project Files:

- `project.py`  
  The main file that contains:
  - The terminal interface (`main()`).
  - All game functions (`tic_tac_toe()`, `rock_paper_scissors()`, `ping_pong()`, `guess_the_number()`).
  - Helper logic such as `decide_winner()`, `did_collide()`, and `update_score()` made accessible for testing.

- `test_project.py`  
  Contains unit tests written with `pytest` to ensure functionality of pure logic functions like:
  - Winner logic in Rock Paper Scissors
  - Collision and scoring in Pong
  - Input and edge cases in Guess the Number

- `requirements.txt`  
  Lists third-party libraries used, such as `pyfiglet` and `cowsay`, required to run the program.

- `README.md`  
  You're reading it! Describes the structure, logic, and purpose of the project.

---

### Features:

- **Tkinter GUI Integration**  
  Each game has its own GUI window with labeled buttons, score tracking, and reset functionality.
  
- **Play Modes**  
  Select between "Play with Friend" and "Play with Computer" in games like Tic Tac Toe and Rock Paper Scissors.

- **Smooth Game Transitions**  
  After each game ends, the player is redirected to the main menu without restarting the program.

- **Clean Modular Code**  
  The codebase is structured to separate game logic from UI code, enabling easier testing and updates.

- **Testing with Pytest**  
  Pure functions such as determining the winner or detecting collisions are tested using automated unit tests.

---

### Design Decisions:

- **Why Tkinter?**  
  Tkinter was chosen for its simplicity and native support in Python, enabling rapid prototyping of GUI games without requiring external dependencies.

- **Why a game suite?**  
  Instead of building a single complex app, I opted to combine multiple small games into one cohesive experience. This approach allowed me to practice modularization, event handling, and testing across diverse game types.

- **Logic Separation**  
  Game logic such as determining the winner, collisions, or score updates is separated from GUI so it can be tested independently using `pytest`.

- **Terminal-Driven Flow**  
  Although the games use GUI, the central menu remains terminal-based for simplicity and to demonstrate command-line interactivity.

---

### Technologies Used:

- Python 3
- Tkinter for GUI
- Pytest for testing
- Pyfiglet and Cowsay for fun CLI output

---

### Installation & Running:

1. Ensure Python 3.10+ is installed
2. Install requirements:

```bash
pip install -r requirements.txt
