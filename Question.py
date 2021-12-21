import csv
import random

from random import shuffle

class Questions():
    
    def __init__(self) :
        self.questionstorage = {}
        self.numberquestion = 'questions.csv'
        self.getquestions(self.numberquestion)


    def getquestions(self,database) :  #function to obtains the questions from the file
     with open(database) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    difficulty = int(row[0])
                    statement = row[1]
                    wrong1 = row[2]
                    wrong2 = row[3]
                    wrong3 = row[4]
                    answer = row[5]
                    currentQuestion = [statement, wrong1 , wrong2, wrong3, answer]
                    if difficulty in self.questionstorage:
                       self.questionstorage[difficulty].append(currentQuestion)
                    else:
                     level = []
                     level.append(currentQuestion)
                    self.questionstorage[difficulty] = level
                line_count += 1


    def getramdonquestion(self, round):
     #method to get a ramdon question

        questionnumber = len(self.questionstorage[round])
        rq = random.randint(0, questionnumber-1)

        return self.questionstorage[round][rq]
       




    

    def congrats(self):

     print("Congratulations you have won")


    def displayCorrectanswer(self):
        print("You have chosen the correct answer, you can advace, but it will get more difficult \n")

    
    def displaywronganswer(self):
        print("You chose the wrong answer, you have lost everything")


    def displayQuestion(self, Question):
        print(str(Question[0])+"\n")
        options = Question[1:]
        shuffle(options)
        for i in options:
            print(i + "\n")
        userInput = input("Write the option you think it is the correct one: ")

        return userInput