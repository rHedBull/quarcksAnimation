from graphics import *

def main():

    win.setBackground("blue")
    center = Point(300,200)
    circ = Circle(center, 50)
    circ.setFill("red")
    circ.draw(win)

    print("this works")
    
    win.getMouse()
    win.close()

win = GraphWin("window",500,500)
main()