import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

class Sun:
   def __init__(self, iname, irad, im, itemp):
       self.name = iname
       self.radius = irad
       self.mass = im
       self.temp = itemp
       self.x = 0
       self.y = 0

       self.sturtle = turtle.Turtle()
       self.sturtle.shape("circle")
       self.sturtle.color("yellow")

   def getName(self):
       return self.name

   def getRadius(self):
       return self.radius

   def getMass(self):
       return self.mass

   def getTemperature(self):
       return self.temp

   def getVolume(self):
       v = 4.0/3 * math.pi * self.radius**3
       return v

   def getSurfaceArea(self):
       sa = 4.0 * math.pi * self.radius**2
       return sa

   def getDensity(self):
       d = self.mass / self.getVolume()
       return d

   def setName(self, newname):
       self.name = newname

   def __str__(self):
       return self.name

   def getXPos(self):
       return self.x

   def getYPos(self):
       return self.y

class Planet:

   def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
       self.name = iname
       self.radius = irad
       self.mass = im
       self.distance = idist
       self.x = idist
       self.y = 0
       self.velx = ivx
       self.vely = ivy
       self.color = ic

       self.pturtle = turtle.Turtle()
       self.pturtle.up()
       self.pturtle.color(self.color)
       self.pturtle.shape("circle")
       self.pturtle.goto(self.x,self.y)
       self.pturtle.down()

   def getName(self):
       return self.name

   def getRadius(self):
       return self.radius

   def getMass(self):
       return self.mass

   def getDistance(self):
       return self.distance

   def getVolume(self):
       v = 4.0/3 * math.pi * self.radius**3
       return v

   def getSurfaceArea(self):
       sa = 4.0 * math.pi * self.radius**2
       return sa

   def getDensity(self):
       d = self.mass / self.getVolume()
       return d

   def setName(self, newname):
       self.name = newname

   def show(self):
        print(self.name)   

   def __str__(self):
       return self.name

   def moveTo(self, newx, newy):
       self.x = newx
       self.y = newy
       self.pturtle.goto(newx, newy)

   def getXPos(self):
       return self.x

   def getYPos(self):
       return self.y

   def getXVel(self):
       return self.velx

   def getYVel(self):
       return self.vely

   def setXVel(self, newvx):
       self.velx = newvx

   def setYVel(self, newvy):
       self.vely = newvy

