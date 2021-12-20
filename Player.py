


class Player:
    def __init__(self):
      
        self.name=""
        self.round = 1
        self.score=0
    

    def setName(self, User):
        self.name= User
        
        print(self.name)



Partici= Player()


user= input("Insert your name")
Partici.setName(user)

