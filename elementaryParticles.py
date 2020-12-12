from graphics import *
from time import sleep
import math

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

        self.window = wind
        self.C = Circle(self.center, self.radius)
        self.C.setFill(self.strongCharge)
        self.T = Text(self.center, self.sign)
        self.T.setFill("white")
        self.T.setSize(20)

        self.C.draw(self.window)
        self.T.draw(self.window)

    def unDraw(self):
        self.C.undraw()
        self.T.undraw()
    
    def toAnti(self):

        oldSign = self.sign
        self.sign = "Anti- " + oldSign

        weak = self.weakCharge
        self.weakCharge = -1 * weak

        electric = self.electricCharge
        self.electricCharge = -1 * electric

        if self.window  == None:
            print("self.window was undefined!!")
        
        self.unDraw()
        self.draw(self.window)

    def move(self, dx, dy):
        c = math.sqrt( dx**2 + dy**2)

        ## calculating animation length##
        k = c/100               ## factor k, if c < or > than 100 pixel
        standardTime = 1.25      ## seconds
        time = k * standardTime ## c = 100 pixel should take 1.25 seconds

        ## calculating steps parameter ##
        timePerStep = 0.01          ## seconds
        steps = time / timePerStep ## amount of steps

        x = dx/steps
        y = dy/steps

        s = 0
        while s < steps:
            sleep(timePerStep)
        
            self.C.move(x,y)
            self.T.move(x, y)
            s = s + 1
        
class UpQuarck(elementaryParticle):
    name = "Up - Quarck"
    sign = "u"
    mass = 2
    weakCharge = 0.5
    electricCharge = 0.66
    spin = 0.5

    def __init__(self, centerPoint, strongCharge):
        super().__init__(self.name, self.sign, centerPoint, self.mass, strongCharge, self.weakCharge, self.electricCharge, self.spin)

class Gluon(elementaryParticle):
    name = "Gluon"
    sign = "g"
    mass = 0
    weakCharge = 0
    electricCharge = 0
    spin = 1

    def __init__(self, centerPoint, strongCharge):
        super().__init__(self.name, self.sign, centerPoint, self.mass, strongCharge, self.weakCharge, self.electricCharge, self.spin)

