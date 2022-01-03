class QuizBrain:

    def __init__(self, add_list):
        self.question_number = 0
        self.score = 0
        self.question_list = add_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
            return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")

    def check_answer(self):
        if self.user_answer.lower() == self.current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The corrent answer was: {self.current_question.answer}. ")
        print(f"Your current score is: {self.score}/{self.question_number}")