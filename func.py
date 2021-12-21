from Question import Questions
from Players import Player


class Game:
    def __init__(self, Player, Questions):
    

        self.play = Player
        self.round = Player.round
        self.score = Player.score
        self.userName = Player.name
        self.quest = Questions
        print(self.round)
    
    def playGame(self):
        #Initiates the game and controls the flow the game, telling the game which round should be played

        while(self.round <= 5):
            newQuestion = self.quest.getramdonquestion(self.round)
            userInput = self.quest.displayQuestion(newQuestion)
            checkPass = self.checkQuestion(newQuestion, userInput)
            if(checkPass==True):
                self.quest.displayCorrectanswer()
                self.updateScore(self.round)
                self.savePlayerScore(self.player)
                continue

            else:
                self.quest.displaywronganswer()
                self.resetScore()
                self.savePlayerScore(self.play)
                
        self.quest.congrats()
            
    def checkQuestion(self, question, userInput):
        #Checks if question is answered correctly
        
        if(question[1] == userInput):
            self.round += 1
            return True
        else:
            return False

    def updateScore(self, round):
        #Updates player score

        if(round == 5):
            self.score += 10000
        else:
            self.score += round*100
            print(self.score, self.round, self.userName)
    
    def resetScore(self):
        #Resets player score to the first level

        self.score = 0
        self.round = 1
        
    def savePlayerScore(self, player):
        #Conection to player object, updates the info on that object

        player.savePlayerInfo(self.userName, self.score, self.round)
