import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        # Main Menu
        self.title_label = tk.Label(root, text="Welcome To Rock Paper Scissors", font=("Helvetica", 20))
        self.title_label.pack(pady=30)

        self.start_button = tk.Button(root, text="Play", command=self.start_game)
        self.start_button.pack(pady=20)
        self.exit_button = tk.Button(root, text="Quit", command=root.quit)
        self.exit_button.pack(pady=20)

    def start_game(self):
        self.clear_widgets()
    

        # Game UI
        self.title_label = tk.Label(self.root, text="Chose Your Move:", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_round("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_round("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_round("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.start_game)
        self.play_again_button.pack(pady=10)

    def play_round(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        if (player_choice == "Rock" and computer_choice == "Scissors") or \
           (player_choice == "Paper" and computer_choice == "Rock") or \
           (player_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        return "You lose!"

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.geometry("500x300")
    root.mainloop()
