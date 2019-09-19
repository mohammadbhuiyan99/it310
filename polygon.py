from cmath import sqrt, tan
from math import radians

class Polygon :
    def area(self):
        pass
    def perimeter(self):
        pass

class Triangle (Polygon):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Isosceles (Triangle):
    def __init__(self, x,y):
        Triangle.__init__(self, x, x, y)

    def area (self):
        altitude = sqrt(self.x*self.x-self.z*self.z/4)
        return altitude*self.z/2;

    def perimeter (self):
        return self.x + self.y +self.z

class EquilateralTriangle (Triangle):
    def __init__(self, x):
        Triangle.__init__(self, x, x, x)

    def area(self):
        return sqrt(3)*self.x*self.x/4;

    def perimetrer(self):
        return self.x + self.x + self.x

class Quadrilateral(Polygon):
    def __init__(self, x,y):
        self.x = x
        self.y = y

class Rectangle(Quadrilateral):
    def _init__(self, x,y):
        Quadrilateral.__init__(self, x, y)
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)

class Square(Quadrilateral):
    def _init__(self, x):
        Quadrilateral.__init__(self, x, x)
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)

class Pentagon(Polygon):
    def __init__(self, size, numberofSide=5):
        self.size = size
        self.numberofSide = numberofSide

    def area(self):
        angle = radians(180/self.numberofSide)
        return self.size*self.size*self.numberofSide/(4*tan(angle));

    def perimeter(self):
        return self.numberofSide*self.size;

class Hexagon(Polygon):
    def __init__(self, size,numberofSide = 6):
        self.size = size
        self.numberofSide = numberofSide

    def area(self):
        angle = radians(180/self.numberofSide)

    def area(self):
        angle = radians(180/self.numberofSide)
        return self.size * self.size * self.numberofSide / (4 * tan(angle));

    def perimeter(self):
        return self.numberofSide*self.size;

class Octagon(Polygon):
    def __init__(self, size,numberofSide = 8):
        self.size = size
        self.numberofSide = numberofSide

    def area(self):
        angle = radians(180 / self.numberofSide)
        return self.size * self.size * self.numberofSide / (4 * tan(angle));

    def perimeter(self):
        return self.numberofSide*self.size;

isosceles = Isosceles(20,30);
print("Isosceles area: " ,isosceles.area())
print(" Isosceles perimeter : ", isosceles.perimeter())
print("\n\n")

equilateralTriangle = EquilateralTriangle(20);
print("Equilateral Triangle Area: " ,equilateralTriangle.area())
print(" Equilateral Triangle perimeter: ", equilateralTriangle.perimeter())
print("\n\n")

rectangle = Rectangle(20,30);
print("Rectangle area: " ,rectangle.area())
print("Rectangle perimeter : ", rectangle.perimeter())
print("\n\n")

square = Square(20, 20);
print("Square Area: " ,square.area())
print("square Perimeter: ", square.perimeter())
print("\n\n")

pentagon = Pentagon(20);
print("Pentagon Area: " ,pentagon.area())
print("Pentagon Perimeter: ", pentagon.perimeter())
print("\n\n")

hexagon = Hexagon(20);
print("Hexagon Area: " ,hexagon.area())
print("Hexagon Perimeter: ",hexagon.perimeter())
print("\n\n")

octagon = Octagon(20);
print("Octagon Area: " ,octagon.area())
print("Octagon Perimeter: ",octagon.perimeter())


