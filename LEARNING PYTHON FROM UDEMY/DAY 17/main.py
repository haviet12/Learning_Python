from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain




list_question=[]

quiz = QuizBrain(q_list=list_question)

for question in question_data:
    question_text=question["text"]
    question_answer = question["answer"]
    question = Question(q_text=question_text, q_answer=question_answer)
    list_question.append(question)
 
while quiz.still_has_question():
    quiz.next_question()

quiz.final()