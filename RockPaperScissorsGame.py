import tkinter as tk
import random

# Choices
choices = ['rock', 'paper', 'scissors']
user_score = 0
comp_score = 0

# Main logic
def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    
    result_text.set(f"You chose {user_choice} | Computer chose {comp_choice}")
    
    if user_choice == comp_choice:
        outcome = "It's a draw!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):
        user_score += 1
        outcome = "✅ You win!"
    else:
        comp_score += 1
        outcome = "❌ Computer wins!"
    
    score_text.set(f"You: {user_score}  |  Computer: {comp_score}")
    result_label.config(text=outcome)

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="🪨📄✂️ Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=10)

score_text = tk.StringVar()
score_text.set("You: 0  |  Computer: 0")
score_label = tk.Label(root, textvariable=score_text, font=("Arial", 14, "bold"))
score_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons
for choice in choices:
    tk.Button(button_frame, text=choice.capitalize(), width=10, font=("Arial", 12),
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=10)

# Run
root.mainloop()

