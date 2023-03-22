
class QuizBrain:
    
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    
    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number +=1

        user_answer = input(f"Q.{self.question_number}: {question.text}(True/False)?: ")
        
        self.check_answer(user_answer,question.answer)
     
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it!\nThe correct answer is: {correct_answer}")
            self.score+=1
            print(f"Your score is: {self.score}/{self.question_number}")
        else:
            print(f"You Wrong!\nThe correct answer is: {correct_answer}")
            print(f"Your score is: {self.score}/{self.question_number}")
            
    def final(self):
         if self.question_number == len(self.question_list):
            print("You've completed the quiz")
            print(f"Your total score was {self.score}/{self.question_number}")
