from pygame_functions import *
import random as r

class Player():
    def __init__(self,x,y,sprite):
        self.x = x
        self.y = y

        self.width = 64
        self.height = 96

        self.sprite = sprite
        self.color = "0"
        self.dir = 0


    def draw(self):
        showSprite(self.sprite)
        moveSprite(self.sprite,self.x,self.y)

    def move(self):

        if keyPressed("A") or keyPressed("left"):
            self.dir = 0
            changeSpriteImage(self.sprite,int(self.color) + self.dir)
            self.x -= 3.5
            if self.x <= 0:
                self.x = 544
        if keyPressed("D") or keyPressed("right"):
            self.dir = 6
            changeSpriteImage(self.sprite,int(self.color) + self.dir)
            self.x += 3.5
            if self.x >= 544:
                self.x = 0

        if keyPressed("1"):
            changeSpriteImage(self.sprite,0 + self.dir)
            self.color = "0"
        if keyPressed("2"):
            changeSpriteImage(self.sprite,1 + self.dir)
            self.color = "1"
        if keyPressed("3"):
            changeSpriteImage(self.sprite,2 + self.dir)
            self.color = "2"
        if keyPressed("4"):
            changeSpriteImage(self.sprite,3 + self.dir)
            self.color = "3"
        if keyPressed("5"):
            changeSpriteImage(self.sprite,4 + self.dir)
            self.color = "4"
        if keyPressed("6"):
            changeSpriteImage(self.sprite,5 + self.dir)
            self.color = "5"

        self.draw()

    def getSprite(self):
        return self.sprite

    def getColor(self):
        return self.color

    def killSprite(self):
        killSprite(self.sprite)

class Carrot():
    def __init__(self,x,y,sprite):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64

        self.sprite = sprite
        self.points = 0

        self.img = 0
        self.speed = 1.5

        self.pointAmount = 0
        self.pointCombo = -1
        self.pointList = [10,20,100,200,500,1000,2000,5000]

        self.health = 3

        
    def draw(self):
        showSprite(self.sprite)
        moveSprite(self.sprite,self.x,self.y)

    def changeImage(self):
        self.img = r.randint(0,5)
        changeSpriteImage(self.sprite,self.img)
        self.draw()

    def move(self):
        self.y += self.speed

        if self.y >= 280:
            hurt = makeSound("Assets/hurt.wav")
            playSound(hurt)
            self.pointCombo = -1
            self.health -= 1
            self.x = r.randint(64,576)
            self.y = 20
            self.changeImage()

        moveSprite(self.sprite,self.x,self.y)

    def colision(self,sprite,spritecolor):
        if touching(self.sprite,sprite):
            if int(spritecolor) == int(self.img):
                if self.pointCombo >= 7:
                    self.pointCombo = 7
                else:
                    self.pointCombo += 1

                print(self.pointCombo)
                pickup = makeSound("Assets/pickup.wav")
                playSound(pickup)
                self.pointAmount += self.pointList[self.pointCombo]
            else:
                hurt = makeSound("Assets/hurt.wav")
                playSound(hurt)
                self.health -=1
                self.pointCombo = -1

            self.x = r.randint(64,576)
            self.y = 20
            self.changeImage()
            return True
        else:
            return False

    def changeSpeed(self):
        self.speed += 0.5
        if self.speed >= 5:
            self.speed = 5

    def getScore(self):
        return self.pointAmount

    def getHealth(self):
        return self.health

    def killSprite(self):
        killSprite(self.sprite)