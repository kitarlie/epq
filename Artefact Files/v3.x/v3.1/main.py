import math, time

#This is the time elapsed within the simulation for each 'tick' to occur.
global tickRate
tickRate = 0.5

#This is a list of all variables during every tick.
projectileInfo = []

#This is representative of the projectile itself.
class projectileClass:

    #This assigns the constants associated with the simulation.
    def __init__(self, projectileAttributes):
        #These are the physical properties of the projectile.
        self.mass = projectileAttributes[0]
        self.crossSectionalArea = projectileAttributes[4]
        self.dragCoefficient = projectileAttributes[5]

        #These are the parameters of projection.
        self.initialVelocity = projectileAttributes[1]
        self.initialHeight = projectileAttributes[2]
        self.angleOfProjection = projectileAttributes[3]

        #These are the environmental variables.
        self.gravityAcceleration = -projectileAttributes[6]
        self.fluidDensity = projectileAttributes[7]

        self.dragConstant = -0.5 * self.fluidDensity * self.dragCoefficient * self.crossSectionalArea

    #This caclulates the vectors acting on the projectile at the moment of projection. Right and upwards are taken as positive.
    def initialvectors(self):
        self.currentVerticalVelocity = math.sin(math.radians(self.angleOfProjection)) * self.initialVelocity
        self.currentHorizontalVelocity = math.sin(math.radians(90 - self.angleOfProjection)) * self.initialVelocity
        self.currentVerticalDrag = (self.currentVerticalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentVerticalVelocity)
        self.currentHorizontalDrag = (self.currentHorizontalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentHorizontalVelocity)
        self.currentVerticalAcceleration = ((self.mass * self.gravityAcceleration) + self.currentVerticalDrag) / self.mass
        self.currentHorizontalAcceleration = self.currentHorizontalDrag / self.mass
        self.currentVerticalDisplacement = 0
        self.currentHorizontalDisplacement = 0
        print(str(math.copysign(1, self.currentVerticalVelocity)))

    #This calculates the vectors acting on the projectile at any given moment.
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
        #This is a record of every variable for each tick.
        tickInfo = [
            self.currentVerticalDisplacement,
            self.currentHorizontalDisplacement,
            self.currentVerticalVelocity,
            self.currentHorizontalVelocity,
            self.currentVerticalDrag,
            self.currentHorizontalDrag,
            self.currentVerticalAcceleration,
            self.currentHorizontalAcceleration
            ]
        return tickInfo

#Grabs inputs from menu program
from menu import inputs as projectileAttributes

#Intialises the projectile, sets up the vectors at t = 0s and stores these in the projectileInfo list.
projectile = projectileClass(projectileAttributes)
projectile.initialvectors()
projectileInfo.append(projectile.printTickInfo())
print(projectile.printTickInfo())

#Counts the number of ticks that have passed. Set to 1 to account for the initial setup.
ticks = 1

#This updates the vectors for each tick and adds the tick info to the list.
while projectile.currentVerticalDisplacement > -projectile.initialHeight:
    projectile.vectors()
    projectileInfo.append(projectile.printTickInfo())
    ticks += 1

for i in projectileInfo:
    print(i)
    print('\n')