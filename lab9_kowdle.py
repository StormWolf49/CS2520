#Name: Nikhil Kowdle
#Lab 9
#This program contains the tasks required for this assignment.

class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def calculate_area(self):
        return self.length*self.width
    
    def __str__(self):
        return f"This is a room of size {self.width}' width x {self.length}' length"
    
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
    def displaySides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def calculate_area(self):
        a, b, c = self.sides[0], self.sides[1], self.sides[2]
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
def main():
    room1 = Room(55, 30)
    print(room1)
    room2 = Room(42, 65)
    print(room2)
    print(f"Room 1: {room1.calculate_area()}; Room 2: {room2.calculate_area()}")

    poly = Polygon(4)
    poly.inputSides()
    poly.displaySides()
    tri = Triangle()
    tri.inputSides()
    tri.displaySides()
    print(f"The area of the triangle is {tri.calculate_area()}")

main()