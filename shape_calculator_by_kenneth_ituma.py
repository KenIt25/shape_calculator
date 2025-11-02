import abc


class Shape(abc.ABC):
    """
    Abstract Base Class for all shapes. Enforces a common interface.
    """
    def __init__(self, color):
        #Encapsulation: Protect internal data
        self._color = color

    #Define an interface method that MUST be implemented by subclasses
    @abc.abstractmethod
    def calculate_area(self):
        """Must be implemented by any concrete shape."""
        pass

    #Encapsulation: Public method to safely expose data
    def get_color(self):
        return self._color

class Rectangle(Shape):
    """
    Inherits from Shape.
    """
    def __init__(self, color, length, width):
        super().__init__(color) #Inherit 'color' attribute
        self._length = length
        self._width = width

    #Polymorphism: Specific implementation for calculate_area
    def calculate_area(self):
        return self._length * self._width

#Inheritance & Polymorphism
class Circle(Shape):
    """
    Inherits from Shape.
    """
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius
        #Encapsulation: Private constant
        self._PI = 3.14159 

    #Polymorphism:
    def calculate_area(self):
        return self._PI * (self._radius ** 2)

print("---Shape Calculator by Kenneth Ituma ---")

#Creating objects
rectangle = Rectangle("Blue", 8, 5)
circle = Circle("Green", 6)
shapes = [rectangle, circle]

#print("\n**1. Demonstrating Polymorphism & Abstraction:**")
for shape in shapes:
    
    area = shape.calculate_area()
    
    #Encapsulation
    color = shape.get_color()
    
    print(f"The {color} {shape.__class__.__name__} has an area of: {area:.2f}")

#Safely accessing data
print(f"The circle's color is: {circle.get_color()}")

print("\n--- Program end ---")
