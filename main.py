
from Players import Player
from func import Game
from Question import Questions

#Initiates game asking the user to give the username and type of user, then it just creates a new game and
#the flow is controlled by the game object

questions = Questions()
player = Player()

startGame = False
while(not(startGame)):
    playerStatus = player.requestPlayerStatus()
    if(playerStatus == "yes"):
        playername = player.requestsname()
        isNew = player.setName(playername)
        if(isNew):
            player.saveNewPlayer(playername)
            startGame = True
            break
        else:
            player.noplayerfound()
            continue
    else:
        playername = player.requestsname()
        isOld = player.loadOldPlayer(playername)
        if(isOld):
            startGame = True
            break
        else:
            player.oldPlayerError()
            continue

newGame = Game(player, questions)
newGame.playGame()

