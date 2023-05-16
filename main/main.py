from pygame_functions import *
from objects import *

def main():
    screenSize(640,480)
    setWindowTitle("Gruniozerca")
    setIcon("Assets\icon.ico")
    setBackgroundImage("Assets\menu.png")

    makeMusic("Assets\menu.wav")
    playMusic(-1)

    waitPress()

    stopMusic()

    setBackgroundImage("Assets\\background.png")

    makeMusic("Assets\game.wav")
    playMusic(-1)

    carrots = makeSprite("Assets\carrots.png",6)
    grunio = makeSprite("Assets\grunios.png",12)

    h1 = makeSprite("Assets\heart.png")
    moveSprite(h1,532,0)

    h2 = makeSprite("Assets\heart.png")
    moveSprite(h2,568,0)

    h3 = makeSprite("Assets\heart.png")
    moveSprite(h3,604,0)

    score = makeLabel("0",32,0,0,'white')
    showLabel(score)

    p = Player(300,320,grunio)
    c = Carrot(0,20,carrots)
    c.changeImage()
    targetTime = 0

    while True:
        time = clock()
        if time>targetTime:
            targetTime = time + 15000
            c.changeSpeed()

        s = p.getSprite()
        col = p.getColor()
        scr = c.getScore()
        h = c.getHealth()

        p.draw()
        p.move()
        c.draw()
        c.move()

        c.colision(s,col)

        if h == 3:
            showSprite(h1)
            showSprite(h2)
            showSprite(h3)
        elif h == 2:
            hideSprite(h3)
        elif h == 1:
            hideSprite(h2)
        elif h == 0:
            hideSprite(h1)

            stopMusic()

            c.killSprite()
            p.killSprite()

            hideAll()
            hideLabel(score)

            setBackgroundImage("Assets\gameover.png")

            gameover = makeSound("Assets\gameover.wav")
            playSound(gameover)
            break

        changeLabel(score,str(scr))
        tick(60)

    endWait()

if __name__ == "__main__":
    main()
