from  tkinter import  *
import requests
import json

# pasiemame duomenis is API panaudodami requests

url = "https://opentdb.com/api.php?amount=1"
response = requests.get(url)
data = json.loads(response.text)
question = data['results'][0]

# parodo klausima ir pasirinkima vartotojui
print(question['question'])
options = question['incorrect_answers'] + [question['correct_answer']]
for option in options:
    print("- " + option)

# paklausiam vartotojo kad atsakytu ir patikrintu ji
user_answer = input("Your answer: ")
if user_answer == question['correct_answer']:
    print("Correct!")
else:
    print("Incorrect. The correct answer is: " + question['correct_answer'])



