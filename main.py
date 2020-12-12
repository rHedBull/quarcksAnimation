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
    initialY = 0.8 * wind.getHeight()

    ## time arrow ##
    pointUpArrow = Point(40, (wind.getHeight()*0.9))
    pointDownArrow = Point(40, (wind.getHeight()*0.1))
    timeArrow = Line(pointUpArrow, pointDownArrow)
    timeArrow.setArrow("last")
    timeArrow.setFill("white")
    timeArrow.setWidth(5)
    timeArrow.draw(wind)

    pHalfArrow = Point(50, (wind.getHeight()*0.5))
    timeText = Text(pHalfArrow, "t")
    timeText.setFill("white")
    timeText.setSize(30)
    timeText.draw(wind)

    ## überschrift
    ## relative to window size !! 


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
    ## u.toAnti() create current x and y position attributes for all classes, change draw, undraw, to Anti methods !!!!!!

    moveWX = 100
    moveWY = -100  
    w.move(moveWX, moveWY)
    

    initialNX = initialWX + moveWX
    initialNY = initialWY + moveWY
    p3 = Point(initialNX, initialNY)
    n = ElektronNeutrino(p3)
    n.draw(wind)

    positron = Positron(p3)
    positron.draw(wind)
    w.unDraw()

    moveNX = 100
    moveNY = -100  
    n.move(moveNX, moveNY)
    positron.move(-moveNX, moveNY)


    u.move(-moveUpQX, moveUpQY)






main()