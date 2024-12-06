import pygame, simpleGE

#leaf
class Leaf(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("leaf1.png")
        self.setSize(35, 35)
        self.reset()
        
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("leaf2.png")
        self.setSize(35, 35)
        self.reset()
        
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("leaf3.png")
        self.setSize(35, 35)
        self.reset()
        
    def reset(self):
        self.y = 3
        self.x = random.randmit (0, self.screenWidth)
        self.dy = random.randit(0,4)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
            
#butterfly
class Butterfly(simpleGE.sprite):
    def __init__(self, scene):
        self.setImage("butterfly.png")
        self.setSize(50, 50)
        self.position = (340, 140)
        self.moveSpeed = 6
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.movespeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x -= self.movespeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.movespeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y -= self.movespeed

#scorekeeping
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0 Leaf(s)"
        self.center = (580, 460)

#time
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 1:30"
        self.center = (80, 480)


        
#background & game
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("picnictable.png")
        
        self.sndLeaf = simpleGE.Sound("leafcrunch.flac")
        
        self.butterfly = Butterfly(self)
        self.numLeafs = 3
        self.leafs = []
        for i in range(self.numLeafs):
            self.leafs.append(Leaf(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        
        self.sprites = [self.butterfly,
                        self.leaf,
                        self.lblScore,
                        self.lblTime]
        
    def process(self):
        for leaf in self.leafs:
            if self.butterfly.collidesWith(leaf):
                self.sndLeaf.play()
                leaf.reset()
                self.score += 1
                self.lblScore.text = f"Score:  Leaf(s){self.score}"
        
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop
        
#instruction
class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("instructionsbackground.png")
        self.setSize(150, 150)
        
        self.response = "Flutter In"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions,textLines = [
            "You are a butterfly",
            "looking for the best",
            "sleeping leaf.",
            "How many can you grab",
            "unitl you find the",
            "right one?"]
        
        self.instructions.center = (75, 100)
        self.instructions.size = (100, 125)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Flutter In"
        self.btnPlay.center = (80, 60)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Flutter Away"
        self.btnQuit.center = (560, 60)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
        
#second process
    def prcoess(self):
        if self.btnQuit.clicked:
            self.response = "Flutter Away"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Flutter In"
            self.stop()
            
    def main():
        keepGoing = True
        score = 0
        while keepGoing:
            instructions = Instructions(score)
            instructions.start()
            
            if instructions.response == "Flutter In":
                game = Game()
                game.start()
                score = game.score
                
            else:
                keepGoing = False
                
                
    if __name__ == "__main__":
        main()
        
#640x480 is standard box size?
#python coordinates will be switched based upon their system, see website.
#will i need to change the instructions background image to specific coordinates
#is 150x150 good for instructions background image, double check? 