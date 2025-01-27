import math, time

global tickrate
tickrate = 0.001

projectileAttributes = []

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
        self.currentVerticalDisplacement += (self.currentVerticalVelocity * tickrate)
        self.currentHorizontalDisplacement += (self.currentHorizontalVelocity * tickrate)
        self.currentVerticalVelocity += (self.currentVerticalAcceleration * tickrate)
        self.currentHorizontalVelocity += (self.currentHorizontalAcceleration * tickrate)
        self.currentVerticalDrag = (self.currentVerticalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentVerticalVelocity)
        self.currentHorizontalDrag = (self.currentHorizontalVelocity ** 2) * self.dragConstant * math.copysign(1, self.currentHorizontalVelocity)
        self.currentVerticalAcceleration = ((self.mass * self.gravityAcceleration) + self.currentVerticalDrag) / self.mass
        self.currentHorizontalAcceleration = self.currentHorizontalDrag / self.mass

    def __str__(self):
        string = 'Current vertical displacement = {} m \nCurrent vertical acceleration = {} m \nCurrent vertical velocity = {} \n\n'.format(self.currentVerticalDisplacement, self.currentVerticalAcceleration, self.currentVerticalVelocity)
        return string


#These are test inputs, to check whether the simulation itself works without needing to code the menu first.
projectileAttributes.append(float(input('mass')))
projectileAttributes.append(float(input('initial velocity')))
projectileAttributes.append(float(input('height')))
projectileAttributes.append(float(input('angle of projection')))
projectileAttributes.append(float(input('cross-sectional area')))
projectileAttributes.append(float(input('drag coefficient')))
projectileAttributes.append(float(input('acceleration due to gravity')))
projectileAttributes.append(float(input('fluid density')))

projectile = projectileClass(projectileAttributes)
projectile.initialvectors()

ticks = 0

while projectile.currentVerticalDisplacement > -projectile.initialHeight:
    projectile.vectors()
    print(projectile)
    ticks += 1
    time.sleep(0.01)

print(str(ticks * tickrate))