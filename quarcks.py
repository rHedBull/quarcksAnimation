from graphics import *
class Quarck(object):

    radius = 50 # not physical radius

    def __init__(self, centerPoint, name, sign, mass, eCharge, wCharge, sCharge):
        self.center = centerPoint
        self.name = name
        self.sign = sign
        self.mass = mass
        self.electricCharge = eCharge
        self.weakCharge = wCharge
        self.strongCharge = sCharge

    def draw(self, win):
        c = Circle(self.center, self.radius)
        c.setFill("grey")

        t = Text(self.center, self.sign)
        t.setSize(20)
        t.setTextColor("white")

        c.draw(win)
        t.draw(win)

    


class Positron(Quarck):
    name = "Positron"
    sign = "e+"
    mass = 0.511
    weakCharge = 0.5
    electricCharge = 1
    strongCharge = 0

    def __init__(self, centerPoint):
        super().__init__(centerPoint, self.name, self.sign, self.mass, self.electricCharge, self.weakCharge, self.strongCharge)

    



