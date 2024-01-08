from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_obj = Question(question['text'], question['answer'])
    question_bank.append(q_obj)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}!")