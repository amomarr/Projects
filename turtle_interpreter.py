#Amal Omar 
#CS 5001
#Project 9
import turtle 
class TurtleInterpreter:
    initialized = False
    def __init__(self, dx = 800, dy = 800):
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
    
    def drawString(self, dstring, distance, angle):
        stack_list = []
        color_stack = []
        for i in range(len(dstring)):
            if dstring[i] == "F":
                turtle.forward(distance)
            elif dstring[i] == "-":
                turtle.right(angle)
            elif dstring[i] == "+":
                turtle.left(angle)
            elif dstring[i] =="[": 
                stack_list.append([turtle.pos(),turtle.heading()])
            elif dstring[i] =="]":    
                turtle.penup()
                getPop= stack_list.pop()
                turtle.setheading(getPop[1])
                turtle.goto(getPop[0])
                turtle.pendown()
            elif dstring[i] == "<": 
                color_stack.append( turtle.color()[0] )
            elif dstring[i] == ">":
                getColor = color_stack.pop()
                turtle.color(getColor)
            elif dstring[i] == "g":
                turtle.color("green")
            elif dstring[i] == "y":
                turtle.color("brown")
            elif dstring[i] == "r":
                turtle.color('#990099','#cc00cc')
            elif dstring[i] == "{": 
                turtle.begin_fill()
            elif dstring[i] == "}": 
                turtle.end_fill()    
        turtle.update()


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a clicks
        turtle.exitonclick()

    def place(self, xpos, ypos, angle=None): 
        self.goto(xpos,ypos)
        if angle != None:
            self.orient(angle)
        #the method should pick up the pen, place the turtle at location (xpos, ypos), orient the turtle if the angle argument is not None, and then put down the pen. Use the appropriate turtle commands to execute this.
    def orient(self, angle): 
        turtle.setheading(angle)
        #the method should use the turtle's setheading function to set turtle's heading to the given angle.
    def goto(self, xpos, ypos): 
        turtle.up()
        turtle.goto(xpos,ypos)
        turtle.down()
        #the method should pick up the turtle, send the turtle to (xpos, ypos), and then put the pen down.
    def setColor(self, c): 
        turtle.color(c) 
    def setWidth(self, w): 
        turtle.width(w) 