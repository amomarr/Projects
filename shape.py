#Amal Omar 
#CS 5001
#Project 9
import turtle_interpreter
class Shape:
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '' ):
        self.distance = distance
        self.angle = angle
        self.color = color
        self.string = istring
    def setColor(self, c):  #set the color field to c
        self.color = c
    def setDistance(self, d): #set the distance field to d
        self.distance = d
    def setAngle(self, a): #set the angle field to a
        self.angle = a 
    def setString(self, s):  #set the string field to s
        self.string = s 

    def draw(self, xpos, ypos, scale=1.0, orientation=0):
        NewObject = turtle_interpreter.TurtleInterpreter()
        NewObject.place(xpos, ypos, orientation)
        NewObject.setColor(self.color)
        NewObject.drawString(self.string, self.distance*scale, self.angle)
        
class Square(Shape):

   def __init__(self, distance=100, color=(0, 0, 0) ):
       Shape.__init__(self, distance, 90, color, "F-F-F-F-")
   
class Triangle(Shape):

   def __init__(self, distance=100, color=(0, 0, 0) ):
       Shape.__init__(self, distance, 120, color, "F-F-F-")

class Rectangle(Shape):

   def __init__(self, distance=100, color=(0, 0, 0) ):
       Shape.__init__(self, distance, 90, color, "{FFF-F-FFF-F-}")

class Pentagon(Shape):

   def __init__(self, distance=100, color=(0, 0, 0) ):
       Shape.__init__(self, distance, 72, color, "{F-F-F-F-F-}")

class Octangon(Shape):

   def __init__(self, distance=100, color=(0, 0, 0) ):
       Shape.__init__(self, distance, 45, color, "{F-F-F-F-F-F-F-F-}")

def test():
    octangon = Octangon()
    octangon.draw(0,0, scale=1.0, orientation=90)
    pentagon = Pentagon()
    pentagon.draw(180,200, scale=1.0, orientation=90)
    rectangle = Rectangle()
    rectangle.draw(-250,-110, scale=1.0, orientation=90)
    square = Square()
    square.draw(-120,-180, scale=1.0, orientation=90)
    triangle= Triangle()
    triangle.draw(-300,-300, scale=1.0, orientation=90)
    turtle_interpreter.hold()

if __name__ == "__main__":
    test()
    
