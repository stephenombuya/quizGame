import tkinter as tk
from tkinter import messagebox
import time
import json
import os

# Path to save high scores
SCORES_FILE = "high_scores.json"


# Utility Functions
def welcome_message():
    print("Welcome to the Computer Quiz!")
    print("You will be asked several questions, and your score will be calculated at the end.")
    print("Let's see how much you know about computer science. Have fun!\n")


def play_quiz():
    score = 0
    total_questions = len(quiz_questions)

    for question, correct_answer in quiz_questions.items():
        user_answer = input(question + " ").strip().lower()
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

    print(f"You answered {score}/{total_questions} questions correctly.")
    print(f"Your final score is: {round((score / total_questions) * 100, 2)}%.\n")


def load_high_scores():
    """Loads high scores from a file."""
    if not os.path.exists(SCORES_FILE):
        return {}
    with open(SCORES_FILE, "r") as file:
        return json.load(file)


def save_high_scores(scores):
    """Saves high scores to a file."""
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file)


# Quiz Question Bank
quiz_data = {
    "Hardware": {
        "What does CPU stand for?": "Central Processing Unit",
        "What does GPU stand for?": "Graphics Processing Unit",
    },
    "Software": {
        "What does OS stand for?": "Operating System",
        "What does IDE stand for?": "Integrated Development Environment",
    },
    "Networking": {
        "What does IP stand for?": "Internet Protocol",
        "What does DNS stand for?": "Domain Name System",
    },
}


# Main Quiz Application Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Quiz")
        self.root.geometry("600x400")

        self.category = None
        self.questions = []
        self.current_question = None
        self.correct_answer = None
        self.score = 0
        self.time_remaining = 10  # Time per question in seconds
        self.high_scores = load_high_scores()

        self.create_start_screen()

    def create_start_screen(self):
        """Creates the start screen with category selection."""
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Computer Quiz!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text="Select a category to begin:", font=("Arial", 14)).pack(pady=10)

        for category in quiz_data.keys():
            tk.Button(
                self.root, text=category, font=("Arial", 12),
                command=lambda c=category: self.start_quiz(c)
            ).pack(pady=5)

        tk.Button(self.root, text="View Leaderboard", font=("Arial", 12), command=self.show_leaderboard).pack(pady=20)

    def start_quiz(self, category):
        """Starts the quiz for the selected category."""
        self.category = category
        self.questions = list(quiz_data[category].items())
        self.score = 0
        self.next_question()

    def next_question(self):
        """Loads the next question or ends the quiz."""
        if self.questions:
            self.current_question, self.correct_answer = self.questions.pop(0)
            self.show_question()
        else:
            self.end_quiz()

    def show_question(self):
        """Displays the current question and starts the timer."""
        self.clear_screen()

        tk.Label(self.root, text=f"Category: {self.category}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=self.current_question, font=("Arial", 16)).pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        tk.Button(self.root, text="Submit", font=("Arial", 12), command=self.check_answer).pack(pady=10)

        self.time_remaining = 10
        self.timer_label = tk.Label(
            self.root, text=f"Time remaining: {self.time_remaining} seconds", font=("Arial", 12)
        )
        self.timer_label.pack(pady=10)
        self.update_timer()

    def update_timer(self):
        """Updates the timer every second."""
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time remaining: {self.time_remaining} seconds")
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(timed_out=True)

    def check_answer(self, timed_out=False):
        """Checks the user's answer."""
        user_answer = self.answer_entry.get().strip().lower()
        if timed_out:
            messagebox.showinfo("Time's up!", f"The correct answer was: {self.correct_answer}")
        elif user_answer == self.correct_answer.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "Great job!")
        else:
            messagebox.showinfo("Incorrect!", f"The correct answer was: {self.correct_answer}")

        self.next_question()

    def end_quiz(self):
        """Displays the final score and updates the leaderboard."""
        self.clear_screen()
        tk.Label(self.root, text=f"Quiz Over! Your Score: {self.score}", font=("Arial", 18)).pack(pady=20)

        if self.category not in self.high_scores or self.score > self.high_scores[self.category]:
            self.high_scores[self.category] = self.score
            save_high_scores(self.high_scores)
            tk.Label(self.root, text="New High Score!", font=("Arial", 14), fg="green").pack(pady=10)

        tk.Button(self.root, text="Play Again", font=("Arial", 12), command=self.create_start_screen).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 12), command=self.root.quit).pack(pady=10)

    def show_leaderboard(self):
        """Displays the leaderboard."""
        self.clear_screen()
        tk.Label(self.root, text="Leaderboard", font=("Arial", 18)).pack(pady=20)

        if not self.high_scores:
            tk.Label(self.root, text="No high scores yet!", font=("Arial", 14)).pack(pady=10)
        else:
            for category, score in self.high_scores.items():
                tk.Label(self.root, text=f"{category}: {score}", font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="Back to Main Menu", font=("Arial", 12), command=self.create_start_screen).pack(pady=20)

    def clear_screen(self):
        """Clears all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()


# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
