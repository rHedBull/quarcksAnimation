from graphics import *
from elementaryParticles import *


window = GraphWin("text",1000, 700)
window.setBackground("blue")

def main():
    ## start button
    headPoint= Point(0.5 * window.getWidth(), 0.1 * window.getHeight())
    heading = Text(headPoint, "Click anywhere to start animation")
    heading.setSize(30)
    heading.setFill("white")
    heading.draw(window)

    window.getMouse()
    heading.undraw()
    weakInteraction(window)

    window.getMouse()
    window.close()

def weakInteraction(wind):
    initialX = 0.1 * wind.getWidth() ## start point UpQuarck
    initialY = 0.9 * wind.getHeight()

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
    headPoint= Point(0.5 * wind.getWidth(), 0.1 * wind.getHeight())
    heading = Text(headPoint, "Schwachewechselwirkung ( Weak Interaction)")
    heading.setSize(30)
    heading.setFill("white")
    heading.draw(wind)

    ## relative to window size !! 

    moveUpQX = wind.getWidth() * 0.3
    moveUpQY = wind.getHeight() *  -0.3

    p = Point(initialX,initialY) 
    u = UpQuarck(p,"green")
    u.draw(wind)

    u.move(moveUpQX, moveUpQY)

    ## W boson ######
    initialWX = initialX + moveUpQX
    initialWY = initialY + moveUpQY
    p2 = Point(initialWX, initialWY)
    w = WplusBoson(p2)
    w.draw(wind)
    u.toAnti() 

    moveWX = wind.getWidth() * 0.1
    moveWY = wind.getHeight() *  -0.1 
    w.move(moveWX, moveWY)
    
    ## neutrino ###########
    initialNX = initialWX + moveWX
    initialNY = initialWY + moveWY
    p3 = Point(initialNX, initialNY)
    n = ElektronNeutrino(p3)
    n.draw(wind)

    ## Positron #################
    positron = Positron(p3)
    positron.draw(wind)
    w.unDraw()

    moveNX = wind.getWidth() * 0.2 - moveWX
    moveNY = wind.getHeight() *  -0.2 - moveWY
    n.move(moveNX, moveNY)
    positron.move(-moveNX, moveNY)


    u.move(-moveUpQX, moveUpQY)



main()