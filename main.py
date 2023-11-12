from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# import os

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
# os.system('clear')
print("You've completed the quiz!!!\n")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
