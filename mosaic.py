#Amal Omar 
#CS 5001
#Project 9
import shape
import turtle_interpreter 

def tile(x, y, scale):
    square = shape.Square()
    square.setDistance(scale) 
    square.draw(x,y, scale, orientation=90)
    octangon = shape.Octangon(color=(0.8,1,0.8))
    octangon.setDistance(scale/4) 
    octangon.draw (x+scale/2, y+scale/2, scale, orientation=90)
    pentagon = shape.Pentagon(color=(0,1,0))
    pentagon.setDistance(scale/4)
    pentagon.draw(x+scale/3, y+scale/3, scale, orientation=90)
    rectangle = shape.Rectangle(color=(0.6,0,0.6))
    rectangle.setDistance(scale/4)
    rectangle.draw(x+scale/4, y+scale/4, scale, orientation=90)
    triangle= shape.Triangle()
    triangle.setDistance(scale/4)
    triangle.draw(x+scale*0.5, y+scale*0.5, scale, orientation=90)
    

def mosaic(x, y, scale, Nx, Ny): 
    hold = turtle_interpreter.TurtleInterpreter()
    for i in range(Nx):
        x = 100*i 
        for j in range(Ny):
            y = 100*j
            tile(x,y, scale)

    hold.hold()
mosaic(0,0,10,3,4)

