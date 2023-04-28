import requests
import json
import tkinter as tk

# paduodam 10 klausimu is API kuri padarom json
url = "https://opentdb.com/api.php?amount=10"
response = requests.get(url)
data = json.loads(response.text)
questions = data['results']

# Isima HTML artifaktus is klausimino ir atsakimu
for question in questions:
    question_text = question['question'].replace("&quot;", "").replace("&amp;", "").replace("&apos;", "").replace("&#039;", "")
    question['question'] = question_text
    incorrect_answers = question['incorrect_answers']
    for i in range(len(incorrect_answers)):
        incorrect_answer_text = incorrect_answers[i].replace("&quot;", "").replace("&amp;", "").replace("&apos;", "").replace("&#039;", "")
        incorrect_answers[i] = incorrect_answer_text
    correct_answer_text = question['correct_answer'].replace("&quot;", "").replace("&amp;", "").replace("&apos;", "").replace("&#039;", "")
    question['correct_answer'] = correct_answer_text

# sukuriam tkinter ekrana
window = tk.Tk()
window.geometry('800x600')
window.title('Trivia')

# apibreziu  globalius kintamuosius
current_question_index = 0
user_score = 0


# parodyti dabartini klausima ir patikrinti vartotojui
def display_question():
    global current_question_index
    global user_score

    # gauti dabartini klausima is klausimu saraso
    question = questions[current_question_index]

    # isvalo ankstesni klausima
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()

    # parodo esama klausima ir parinktis
    question_label.config(text=question_text)
    options = question['incorrect_answers'] + [question['correct_answer']]
    for i, option in enumerate(options):
        option_button = tk.Button(window, text=f"{i + 1}. {option}", command=lambda ans=option: check_answer(ans))
        option_button.pack()


# su funkcija patikriname atsakyma vartotojo
def check_answer(user_answer):
    global current_question_index
    global user_score

    # gauti dabartini klausima is klausimu saraso
    question = questions[current_question_index]

    if user_answer == question['correct_answer']:
        user_score += 1
        result_label.config(text='Correct!', fg='green')
    else:
        result_label.config(text=f"Incorrect. The correct answer is: {question['correct_answer']}", fg='red')

    # didina klausimus indexe ir tikrina ar buvo parodyti visi klausimai
    current_question_index += 1
    if current_question_index == len(questions):
        # parodyk paskutini rezultata ir isjungti buttonus
        score_label.config(text=f"Final Score: {user_score}/{len(questions)}")
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')
    else:
        # parodyk kita klausima
        window.after(1000, display_question)


# parodo esama klausima per label
question_label = tk.Label(window, text='')
question_label.pack()

# sukuriam label kad parodyti rezultatas
result_label = tk.Label(window, text='')
result_label.pack()

# sukuria label pavaizduoti vartotojo taskus
score_label = tk.Label(window, text='')
score_label.pack()

# pavaizduoja pirma klausima
display_question()

window.mainloop()
