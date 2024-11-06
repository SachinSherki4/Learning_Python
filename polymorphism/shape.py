'''
Created on Oct 29, 2024

@author: ssherki
'''
import math

class Shape :
    
    def area(self):
        raise NotImplementedError("Subclass must implement Abstract Method")

class Circle(Shape) :
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        # calculate area of circle
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width=width
        self.height=height
    
    def area(self):
        # calculate area of rectangle 
        return self.width * self.height
        
        
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return 0.5 * self.base * self.height

def print_area(Shape):
    print(f"The area of Shape is : {shape.area():.2f}")

if __name__ == "__main__":
    circle = Circle(5)
    rectangle=Rectangle(5,8)
    triangle=Triangle(6,8)

    shapes=[circle,rectangle,triangle]
    for shape in shapes:
        print_area(Shape)
        


        
        
        
        