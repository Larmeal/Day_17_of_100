from new_data import new_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in new_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(add_text=question_text, add_answer=question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()