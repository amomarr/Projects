import shape
import lsystem
import turtle_interpreter

class Tree(shape.Shape):

    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        shape.Shape.__init__(self, distance, angle, color)
        self.iterations = iterations
        self.lsystem = lsystem.Lsystem(filename)
    def setIterations(self, N):
        self.iterations = N
    def read(self, filename):
        self.lsystem.read(filename)
    def draw(self, xpos, ypos, scale=1.0, orientation=90):
        self.string = self.lsystem.buildString(self.iterations)
        shape.Shape.draw(self, xpos, ypos, scale, orientation)

def test(file):
    BigTree = Tree()
    BigTree.read(file)
    BigTree.draw(-100,5, scale=1.0, orientation=90)
    MediumTree = Tree()
    MediumTree.read(file)
    MediumTree.draw(0,5, scale=1.0, orientation=90)
    SmallTree = Tree()
    SmallTree.read(file)
    SmallTree.draw(100,5, scale=1.0, orientation=90)
    SmallTree.hold() #hold methods doesn't work here and i dont know why but it works in the turtle_interpreter
    
    
    
    

if __name__ == "__main__":
    test('systemJ.txt')