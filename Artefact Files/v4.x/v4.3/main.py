import math

#A list of all variables during every tick
projectileInfo = []

#Rrepresents the projectile itself
class projectileClass:

    #Assigns the inputs values
    def __init__(self, projectileAttributes):
        #Physical properties of the projectile
        self.mass = projectileAttributes[0]
        self.crossSectionalArea = projectileAttributes[4]
        self.dragCoefficient = projectileAttributes[5]

        #Parameters of projection.
        self.initialVelocity = projectileAttributes[1]
        self.initialHeight = projectileAttributes[2]
        self.angleOfProjection = projectileAttributes[3]

        #Environmental variables.
        self.gravityAcceleration = -projectileAttributes[6]
        self.fluidDensity = projectileAttributes[7]

        self.dragConstant = -0.5 * self.fluidDensity * self.dragCoefficient * self.crossSectionalArea

    #Caclulates the vectors acting on the projectile at the moment of projection. 
    #Right and upwards are taken as positive.
    def initialVectors(self):
        self.currentVerticalVelocity = math.sin(math.radians(self.angleOfProjection)) * self.initialVelocity
        self.currentHorizontalVelocity = math.sin(math.radians(90 - self.angleOfProjection)) * self.initialVelocity
        self.currentVerticalDrag = (self.currentVerticalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentVerticalVelocity)
        self.currentHorizontalDrag = (self.currentHorizontalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentHorizontalVelocity)
        self.currentVerticalAcceleration = ((self.mass * self.gravityAcceleration) + self.currentVerticalDrag) / self.mass
        self.currentHorizontalAcceleration = self.currentHorizontalDrag / self.mass
        self.currentVerticalDisplacement = 0
        self.currentHorizontalDisplacement = 0

    #Updates the vectors acting on the projectile
    def vectors(self):
        self.currentVerticalDisplacement += (self.currentVerticalVelocity * tickRate)
        self.currentHorizontalDisplacement += (self.currentHorizontalVelocity * tickRate)
        self.currentVerticalVelocity += (self.currentVerticalAcceleration * tickRate)
        self.currentHorizontalVelocity += (self.currentHorizontalAcceleration * tickRate)
        self.currentVerticalDrag = (self.currentVerticalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentVerticalVelocity)
        self.currentHorizontalDrag = (self.currentHorizontalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentHorizontalVelocity)
        self.currentVerticalAcceleration = ((self.mass * self.gravityAcceleration) + self.currentVerticalDrag) / self.mass
        self.currentHorizontalAcceleration = self.currentHorizontalDrag / self.mass

    def printTickInfo(self):
        #Records every vector for each tick.
        tickInfo = [
            self.currentVerticalDisplacement,
            self.currentHorizontalDisplacement,
            self.currentVerticalVelocity,
            self.currentHorizontalVelocity,
            self.currentVerticalAcceleration,
            self.currentHorizontalAcceleration,
            self.currentVerticalDrag,
            self.currentHorizontalDrag,
            ]
        return tickInfo

#Grabs inputs from menu program
from initialmenu import inputs as projectileAttributes

#Time elapsed within the simulation for each 'tick' to occur.
global tickRate
tickRate = projectileAttributes[8]

#Intialises the projectile, sets up the vectors at t = 0s and stores these in the projectileInfo list.
projectile = projectileClass(projectileAttributes)
projectile.initialVectors()


#Updates the vectors for each tick and adds the tick info to the list.
while projectile.currentVerticalDisplacement >= -projectile.initialHeight:
    projectileInfo.append(projectile.printTickInfo())
    projectile.vectors()


import afterparty
quit()