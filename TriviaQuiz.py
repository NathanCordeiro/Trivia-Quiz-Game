import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage

class TriviaQuiz:
    def __init__(self, master, questions):
        self.master = master
        self.master.configure(bg="#00FFFF")  # Set background color of the root window
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.time_expired = False  # Flag to track if time has expired
        self.timer_cancelled = False  # Flag to track if timer is cancelled

        self.question_label = tk.Label(master, text="", font=("Arial", 14), bg="#00FFFF", fg="black")
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for _ in range(4):
            button = tk.Button(master, text="", background="#6699FF",font=("Arial", 12))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", maximum=10)
        self.progress_bar.pack(fill="x", padx=10, pady=5)

        self.quit_button = tk.Button(master, text="Quit", background="red", command=self.quit_game, font=("Arial", 12))
        self.quit_button.pack(pady=40)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question, options, correct_answer = self.questions[self.current_question_index]
            self.question_label.config(text=question)
            for i, option in enumerate(options):
                self.answer_buttons[i].config(text=option, command=lambda ans=option: self.check_answer(ans, correct_answer))
            self.current_question_index += 1
            self.time_expired = False  # Reset the time expired flag
            self.start_timer()
        else:
            self.show_result()

    def start_timer(self):
        self.cancel_timer()  # Cancel any existing timer
        self.timer = 10
        self.progress_bar["value"] = self.timer
        self.update_timer()

    def update_timer(self):
        if self.timer > 0 and not self.time_expired and not self.timer_cancelled:  # Check if time has not expired
            self.timer_id = self.master.after(1000, self.update_timer)
            self.timer -= 1
            self.progress_bar["value"] = self.timer
        elif self.timer == 0 and not self.time_expired:  # Check if time has just expired
            self.time_expired = True  # Set the time expired flag
            self.show_message("Time's Up!", "Sorry, you ran out of time.")
            self.next_question()

    def cancel_timer(self):
        if hasattr(self, 'timer_id'):
            self.master.after_cancel(self.timer_id)

    def check_answer(self, selected_answer, correct_answer):
        if selected_answer == correct_answer:
            self.score += 1
        self.next_question()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_result(self):
        self.show_message("Quiz Over", f"You've completed the quiz!\nYour score: {self.score}/{len(self.questions)}")
        self.timer_cancelled = True

    def quit_game(self):
        self.master.destroy()

class MenuPage:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#00FFFF")  # Set background color of the root window

        self.title_label = tk.Label(master, text="Trivia Quiz", pady="10", font=("Courier", 24), bg="#00FFFF", fg="black")
        self.title_label.pack(pady=0)

        # Load the image
        image_path = 'Trivia.png'  # Replace with the path to your image file
        photo = PhotoImage(file=image_path)

        # Create the image label
        self.image_label = tk.Label(master, image=photo, bg="#00FFFF", pady="10")
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=0)  # Adjust padding as needed

        self.description_label = tk.Label(master, text="Test your knowledge with our fun trivia quiz!", font=("Courier", 12), bg="#00FFFF", fg="black")
        self.description_label.pack(pady=10)

        self.play_button = tk.Button(master, text="Play Game", pady="20", font=("Arial", 14), background="#6699FF", command=self.start_game)
        self.play_button.pack(pady=0)

    def start_game(self):
        self.master.destroy()  # Close the menu page
        root = tk.Tk()
        root.title("Trivia Quiz")
        root.geometry("650x450")

        # Define the questions and answers
        questions = [
        ("Which planet in our solar system has the most moons?", ["Earth", "Mars", "Jupiter", "Saturn"], "Saturn"),
        ("Which mathematician is known for his Last Theorem,\n which took over 350 years to prove?", ["Isaac Newton", "Carl Friedrich Gauss", "Pierre de Fermat", "Euclid"], "Pierre de Fermat"),
        ("Which physicist developed the quantum theory of radiation?", ["Albert Einstein", "Max Planck", "Niels Bohr", "Werner Heisenberg"], "Max Planck"),
        ("Which country has won the most Nobel Prizes in Literature?", ["France", "United States", "United Kingdom", "Germany"], "France"),
        ("Which ancient civilization built the Machu Picchu complex in Peru?", ["Aztec", "Inca", "Maya", "Olmec"], "Inca"),
        ("Which philosopher is known for the quote 'I think, therefore I am'?",["Plato","Aristotle","René Descartes","Immanuel Kant"],"René Descartes"),
        ("Which ancient civilization used a writing system called cuneiform?", ["Egyptians", "Greeks", "Sumerians", "Romans"], "Sumerians"),
        ("Who discovered the structure of DNA?", ["Charles Darwin", "James Watson and Francis Crick", "Gregor Mendel", "Rosalind Franklin"], "James Watson and Francis Crick"),
        ("Which ancient Greek philosopher tutored Alexander the Great?", ["Socrates", "Plato", "Aristotle", "Pythagoras"], "Aristotle"),
        ("Which is the only country, to have played\n in every World Cup since its inception in 1930?", ["Brazil", "Germany", "Italy", "Argentina"], "Brazil")
        ]
        quiz = TriviaQuiz(root, questions)
        root.mainloop()

# Create the Tkinter window and start the quiz
root = tk.Tk()
root.title("Trivia Quiz")
root.geometry("750x650")

menu = MenuPage(root)
root.mainloop()

