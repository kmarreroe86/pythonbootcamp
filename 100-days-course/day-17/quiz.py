from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# for data in question_data:
#     q = Question(data["text"], data["answer"])
#     question_bank.append(q)
question_bank = [
    Question(data["text"], data["answer"]) for data in question_data
]

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

# print(question_bank)
print("You have completed the quiz")
print(f"Your final score was: {quizBrain.score}/{quizBrain.question_number}")
