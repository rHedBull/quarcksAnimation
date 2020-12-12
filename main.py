from graphics import *
from elementaryParticles import *


window = GraphWin("text",1500, 700)
window.setBackground("blue")

def main():
    weakInteraction(window)
    window.getMouse()
    window.close()

def weakInteraction(wind):
    initialX = 0.1 * wind.getWidth() ## start point UpQuarck
    initialY = 0.9 * wind.getHeight()

    moveUpQX = 100
    moveUpQY = -100

    p = Point(initialX,initialY) 
    u = UpQuarck(p,"green")
    u.draw(wind)

    u.move(moveUpQX, moveUpQY)

    initialWX = initialX + moveUpQX
    initialWY = initialY + moveUpQY
    p2 = Point(initialWX, initialWY)
    w = WplusBoson(p2)
    w.draw(wind)

    moveWX = 100
    moveWY = -100  
    w.move(moveWX, moveWY)

    u.move(-moveUpQX, moveUpQY)

    




main()
window.getMouse()