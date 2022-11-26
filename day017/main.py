from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]

for i in question_data:
    question_text = i["text"]
    question_answer = i['answer']
    new_question = QuestionModel(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You Have Completed The Quiz")
print(f"Final Score: {quiz.score}/{quiz.question_number}")