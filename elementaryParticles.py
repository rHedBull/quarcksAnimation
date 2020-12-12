from graphics import *

class elementaryParticle():

    radius = 50
    offsetPoint = Point(-1,-1)
    C = Circle(offsetPoint,0)
    T = Text(offsetPoint, "")

    def __init__(self, name, sign, centerPoint, mass, strongCharge, weakCharge, electricCharge, spin):
        self.name = name
        self.sign = sign
        self.center = centerPoint
        self.mass = mass
        self.strongCharge = strongCharge
        self.weakCharge = weakCharge
        self.electricCharge = electricCharge
        self.spin = spin

#### getters #########################

    def get_name(self):
        return self.name

    def get_sign(self):
        return self.sign

    def get_center(self):
        return self.center

    def get_mass(self):
        return self.mass

    def get_strongCharge(self):
        return self.strongCharge

    def get_weakCharge(self):
        return self.weakCharge

    def get_electricCharge(self):
        return self.electricCharge
    
    def get_spin(self):
        return self.spin

########################################

    def draw(self, wind):
        self.C = Circle(self.center, self.radius)
        self.T = Text(self.center, self.sign)
        self.T.setFill("red")
        self.T.setSize(30)

        self.C.draw(wind)
        self.T.draw(wind)

    def unDraw(self):
        self.C.undraw()
        self.T.undraw()
    
    def toAnti(self):
        weak = self.weakCharge
        self.weakCharge = -1 * weak

        electric = self.electricCharge
        self.electricCharge = -1 * electric

    def move(self, dx, dy):
        
        self.C.move(dx, dy)
        self.T.move(dx, dy)
        

    


class UpQuarck(elementaryParticle):
    name = "Up - Quarck"
    sign = "u"
    mass = 2
    weakCharge = 0.5
    electricCharge = 0.66
    spin = 0.5

    def __init__(self, centerPoint, strongCharge):
        super().__init__(self.name, self.sign, centerPoint, self.mass, strongCharge, self.weakCharge, self.electricCharge, self.spin)



