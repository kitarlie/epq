import math
import time

global tickrate
tickrate = 0.5 

projectileAttributes = []

class environmentClass:
    #This is representative of the planet on which the projectile undergoes its motion.
    def __init__(self, airDensity, acceleration):
        self.airDensity = airDensity
        self.acceleration = acceleration

class projectileClass:
    #This is representative of the projectile itself.
    def __init__(self, projectileAttributes):
        #These are the physical properties of the projectile.
        self.mass = projectileAttributes[0]
        self.crossSectionalArea = projectileAttributes[4]
        self.dragCoefficient = projectileAttributes[5]

        #These are the parameters of projection.
        self.initialVelocity = projectileAttributes[1]
        self.initialHeight = projectileAttributes[2]
        self.angleOfProjection = projectileAttributes[3]

        #These are the vectors acting on the projectile at any given moment. 
        #The None values are used because the projectile doesn't have any 'current' values yet.
        self.currentVerticalVelocity = None
        self.currentHorizontalVelocity = None
        self.currentVerticalAcceleration = None
        self.currentHorizontalAcceleration = None
        self.currentVerticalDrag = None
        self.currentHorizontalDrag = None

    def setInitialVelocity(self):
        #This calculates the vertical and horizontal components of the projectile's velocity.
        self.currentVerticalVelocity = math.sin(math.radians(self.angleOfProjection)) * self.initialVelocity
        self.currentHorizontalVelocity = math.sin(math.radians(self.angleOfProjection)) * self.initialVelocity


#These are test inputs, to check whether the simulation itself works without needing to code the menu first.
projectileAttributes.append(float(input('mass')))
projectileAttributes.append(float(input('initial velocity')))
projectileAttributes.append(float(input('height')))
projectileAttributes.append(float(input('angle of projection')))
projectileAttributes.append(float(input('cross-sectional area')))
projectileAttributes.append(float(input('drag coefficient')))

projectile = projectileClass(projectileAttributes)
print(str(projectile.mass))
projectile.setInitialVelocity()
print(str(projectile.currentVerticalVelocity))