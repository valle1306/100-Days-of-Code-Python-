from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#Write a for loop to iterate over the question_data
#Create a Question object from each entry in question_data
#Append each Question object to the Question_bank

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# while if quiz still have question remaining:
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}")