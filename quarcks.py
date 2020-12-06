from graphics import *
class Quarck(Circle):

    radius = 50 # not physical radius

    def __init__(self, centerPoint, name, sign, mass, eCharge, wCharge, sCharge):

        super().__init__(centerPoint, self.radius)

        self.name = name
        self.sign = sign
        self.mass = mass
        self.electricCharge = eCharge
        self.weakCharge = wCharge
        self.strongCharge = sCharge

######### Getters ####################
    def get_name(self):
        return self.name

    def get_sign(self):
        return self.sign

    def get_mass(self):
        return self.mass

    def get_electricCharge(self):
        return self.electricCharge

    def get_weakCharge(self):
        return self.weakCharge

    def get_strongCharge(self):
        return self.strongCharge
########################################

    def draw(self, win):
        c = super().draw(win)
        c.setFill("grey")

        t = Text(self.getCenter(), self.sign)
        t.setSize(20)
        t.setTextColor("white")

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

    



