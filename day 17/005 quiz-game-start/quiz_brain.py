class QuizBrain: 
    
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
        
    def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        else: 
            return True
        
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (TRUE/FALSE): ")
        self.check_answer(user_answer, question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
            self.score += 1
        else: 
            print(f"wrong, the coreect answer was {correct_answer}")
        print(f"You've got {self.score} right so far!\n")