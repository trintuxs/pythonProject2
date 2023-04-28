import requests
import tkinter
import random

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices


class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """To check if the quiz has more questions"""

        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""

        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user's answer against the correct answer and maintain the score"""

        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage."""

        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
            self.quiz = quiz_brain
            self.window = Tk()
            self.window.title("iQuiz App")
            self.window.geometry("850x530")

            # Display Title
            self.display_title()

            # Creating a canvas for question text, and dsiplay question
            self.canvas = Canvas(width=800, height=250)
            self.question_text = self.canvas.create_text(400, 125,
                                                         text="Question here",
                                                         width=680,
                                                         fill=THEME_COLOR,
                                                         font=(
                                                             'Ariel', 15, 'italic')
                                                         )
            self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
            self.display_question()

            # Declare a StringVar to store user's answer
            self.user_answer = StringVar()

            # Display four options(radio buttons)
            self.opts = self.radio_buttons()
            self.display_options()

            # To show whether the answer is correct or wrong
            self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
            self.feedback.place(x=300, y=380)

            # Next and Quit Button
            self.buttons()

            # Mainloop
            self.window.mainloop()

    def display_title(self):
        """To display title"""

        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)