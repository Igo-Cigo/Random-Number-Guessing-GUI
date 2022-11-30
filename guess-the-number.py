import tkinter as tk
from tkinter.ttk import *
import random
import os

# for taskbar icon

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

root = tk.Tk()
# root['background'] = '#856ff8'  # ? Debug
root.title("Number Guessing game")
root.geometry('270x480')
root.resizable(0,0)

img = tk.PhotoImage(file="icon.png")
root.iconphoto(False, img)

MAX_LENGHT = 0
RANDOM_NUMBER = 0
GUESS = 0
ROUND = 0
TRIES = 5
WINS = 0
WIN_STREAK = 0
GATE_PASSAGE_FOR_STREAK = 0


def GET_MAX_LENGHT():
    global RANDOM_NUMBER
    global ROUND
    global TRIES
    global GATE_PASSAGE_FOR_STREAK
    global WIN_STREAK
    if GATE_PASSAGE_FOR_STREAK == 0:
        WIN_STREAK = 0
    else:
        GATE_PASSAGE_FOR_STREAK = 0
    TRIES = 5
    streak_label.config(text=f"Win streak: {WIN_STREAK}")
    guesses_left.config(text=f"Guesses left: {TRIES}")
    higher_or_lower.forget()
    SUBMIT_GUESSED_NUMBER.pack()
    higher_or_lower.config(text="")
    higher_or_lower.pack()
    MAX_LENGHT = textbox.get(1.0, "end-1c")
    max_number_label.config(text=f"Maximum lenght: {int(MAX_LENGHT)}")
    ROUND += 1
    round_label.config(text=f"Round: {ROUND}")
    RANDOM_NUMBER = random.randint(1, int(MAX_LENGHT))
    print(f"Random number is: {RANDOM_NUMBER}")
    print(f"Round is: {ROUND}")


def GUESS_NUMBER():
    global TRIES
    global WINS
    global WIN_STREAK
    global GATE_PASSAGE_FOR_STREAK
    GUESS = int(guess_textbox.get(1.0, "end-1c"))
    if GUESS > RANDOM_NUMBER:
        higher_or_lower.config(text="The number is less than guessed")
        TRIES -= 1
        guesses_left.config(text=f"Guesses left: {TRIES}")
        GAME_OVER()
    if GUESS < RANDOM_NUMBER:
        higher_or_lower.config(text="The number is more than guessed")
        TRIES -= 1
        guesses_left.config(text=f"Guesses left: {TRIES}")
        GAME_OVER()
    if GUESS == RANDOM_NUMBER:
        higher_or_lower.config(text="Congrats! You guessed the right number")
        WINS += 1
        WIN_STREAK += 1
        GATE_PASSAGE_FOR_STREAK = 1
        streak_label.config(text=f"Win streak: {WIN_STREAK}")
        wins_label.config(text=f"Wins: {WINS}")
        
def GAME_OVER():
    global GATE_PASSAGE_FOR_STREAK
    global TRIES
    global WIN_STREAK
    print(GATE_PASSAGE_FOR_STREAK)
    if TRIES <= 0:
        higher_or_lower.config(text="You lost! Try another round")
        SUBMIT_GUESSED_NUMBER.forget()
            

# Top


input_max_container = tk.Frame(root)
input_max_container.pack(anchor=tk.CENTER, padx=20, pady=20)

max_number_label = tk.Label(input_max_container, text="Choose the max number:")
max_number_label.pack(pady=(10, 0))

textbox = tk.Text(input_max_container, height=1, width=15)
textbox.pack(pady=(2, 10))

SUBMIT_MAX_NUMBER = tk.Button(
    input_max_container, text="New Game", command=GET_MAX_LENGHT)
SUBMIT_MAX_NUMBER.pack()

# Middle

center_submit_container = tk.Frame(root)
center_submit_container.pack(anchor=tk.CENTER, padx=20, pady=20)

guess_submit_label = tk.Label(center_submit_container, text="Your guess: ")
guess_submit_label.pack()

guess_textbox = tk.Text(center_submit_container, height=1, width=15)
guess_textbox.pack(pady=(2, 10))

SUBMIT_GUESSED_NUMBER = tk.Button(
    center_submit_container, text="Submit guess", command=GUESS_NUMBER)
SUBMIT_GUESSED_NUMBER.pack()

higher_or_lower = tk.Label(center_submit_container)
higher_or_lower.pack()

# Bottom

game_stats_container = tk.Frame(root)
game_stats_container.pack(anchor=tk.CENTER, side="bottom", padx=20, pady=20)

guesses_left = tk.Label(game_stats_container, text=f"Guesses left: {TRIES}")
guesses_left.pack()

round_label = tk.Label(game_stats_container, text=f"Round: {ROUND}")
round_label.pack()

wins_label = tk.Label(game_stats_container, text=f"Wins: {WINS}")
wins_label.pack()

streak_label = tk.Label(game_stats_container, text=f"Win streak: {WIN_STREAK}")
streak_label.pack()

root.mainloop()
