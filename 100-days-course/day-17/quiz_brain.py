class QuizBrain:

    def __init__(self, questions) -> None:
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    
    def next_question(self):
        currentQuestion = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {currentQuestion.text} (True/False): ")
        self.question_number += 1
        self.check_answer(currentQuestion.answer, user_answer)


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    
    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
            
        print(f"Your current score is: {self.score}/{self.question_number} \n")
