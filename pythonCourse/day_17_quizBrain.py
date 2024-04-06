from day_17_question import Question
from day_17_data import question_data
questions = []
for sampleQuestion in question_data:
    text = sampleQuestion["text"]
    answer=  sampleQuestion["answer"]
    questions.append(Question(text, answer))

class QuizBrain:
    questionsRight = 0
    def __init__(self):
        pass
    
    def startQuiz(self):
        index = 0
        while index<len(questions):
            self.askQuestion(index)
            index+=1
        print(f"You got {self.questionsRight} out of {len(questions)} correct!")

    def askQuestion(self, index):
        answer = input(f"True or False? {questions[index].question}\n")
        if answer == questions[index].correctAnswer:
            print("Correct!")
            self.questionsRight+=1
        else:
            print(f"The correct answer was {questions[index].correctAnswer}")

