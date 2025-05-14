import os
from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#4fc3f7")

# Load Images
rock_img = ImageTk.PhotoImage(Image.open("images/rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("images/paper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("images/scissors-user.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open("images/rock.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("images/paper.png"))
scissors_comp_img = ImageTk.PhotoImage(Image.open("images/scissors.png"))

# Scores
user_score = 0
computer_score = 0
round_counter = 0

# Labels
user_label = Label(root, image=scissors_img, bg="#4fc3f7")
comp_label = Label(root, image=scissors_comp_img, bg="#4fc3f7")
comp_label.grid(row=1, column=1, padx=20, pady=20)
user_label.grid(row=1, column=3, padx=20, pady=20)

playerScore = Label(root, text=user_score, font=("Arial", 40, "bold"), bg="#4fc3f7", fg="white")
computerScore = Label(root, text=computer_score, font=("Arial", 40, "bold"), bg="#4fc3f7", fg="white")
computerScore.grid(row=1, column=2)
playerScore.grid(row=1, column=4)

user_indicator = Label(root, font=("Arial", 20, "bold"), text=": USER :", bg="#4fc3f7", fg="white")
comp_indicator = Label(root, font=("Arial", 20, "bold"), text=": COMPUTER :", bg="#4fc3f7", fg="white")
user_indicator.grid(row=0, column=4, padx=20)
comp_indicator.grid(row=0, column=2, padx=20)

msg = Label(root, font=("Arial", 20, "bold"), bg="#4fc3f7", fg="white")
msg.grid(row=3, column=2, columnspan=2, pady=20)

round_label = Label(root, font=("Arial", 16, "bold"), text="Rounds Played: 0", bg="#4fc3f7", fg="white")
round_label.grid(row=4, column=2, columnspan=2, pady=10)

# Update functions
def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    global user_score
    user_score += 1
    playerScore.config(text=str(user_score))

def updateCompScore():
    global computer_score
    computer_score += 1
    computerScore.config(text=str(computer_score))

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "scissors":
        if computer == "rock":
            updateMessage("You lose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()

def updateChoice(x):
    global round_counter
    compChoice = choices[randint(0, 2)]
    
    # Update computer image
    if compChoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissors_comp_img)

    # Update user image
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkWin(x, compChoice)
    
    round_counter += 1
    round_label.config(text=f"Rounds Played: {round_counter}")

choices = ["rock", "paper", "scissors"]

# Buttons
rock = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="ROCK",
              bg="#e74c3c", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1, padx=10, pady=10)

paper = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="PAPER",
               bg="#f1c40f", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2, padx=10, pady=10)

scissors = Button(root, width=20, height=2, font=("Arial", 10, "bold"), text="SCISSORS",
                  bg="#3498db", fg="white", command=lambda: updateChoice("scissors"))
scissors.grid(row=2, column=3, padx=10, pady=10)

# Reset function
def reset_game():
    global user_score, computer_score, round_counter
    user_score = 0
    computer_score = 0
    round_counter = 0
    playerScore.config(text=str(user_score))
    computerScore.config(text=str(computer_score))
    round_label.config(text=f"Rounds Played: {round_counter}")
    user_label.configure(image=scissors_img)
    comp_label.configure(image=scissors_comp_img)
    updateMessage("Make your choice!")


reset_button = Button(root, text="Reset Game", font=("Arial", 25, "bold"),
                      bg="#2ECC71", fg="white", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=5, pady=30)


root.mainloop()
