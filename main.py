from graphics import *
from quarcks import *



def main():

    win.setBackground("blue")
    
    p1 = Point(100,300)
    p2 = Point( 200, 300)
    w = 10

    l = Line(p1,p2)
    l.setWidth(w)
    l.setFill("red")
    l.setArrow("last")

    l.draw(win)

    # test for looping
    i = w
    while i < 200:
        i = i * 1.001
        l.setWidth(i)
        win.redraw()

    print("this works")
    
    win.getMouse()
    win.close()


    
win = GraphWin("window",500,500)
#main()

# q = Quarck(1)

# print(q.get_weakCharge())

p1 = Point(300,300)
p = Positron(p1)
p.draw(win)
p.move(-200,0)


win.getMouse()
