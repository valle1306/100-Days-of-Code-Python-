#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

#Attributes
#question_number =0
# question_list which is going to be initialized later

#Methods: next_questions()
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
         #Initialize the question_list to an input
        self.question_list = q_list

    def still_has_question(self):
        """Return a boolean depending on the value of question_number"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieve the item at the current question_number from the question_list
                Use the input() function to show the user the Question text and ask for the user's answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")