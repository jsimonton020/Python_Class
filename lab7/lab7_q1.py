class Rectangle:

    # contructor has 2 data fields, width & height, default 1 and 2 respectivly
    def __init__(self, width=1, height=2):
        self.height = height
        self.width = width

    # method for returning the area
    def get_area(self):
        return round(self.width * self.height, 2)

    # method for returning perimeter
    def get_perimeter(self):
        return round(2 * (self.width + self.height), 2)

    # a clean way to display the attributes
    def display(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", self.get_area())
        print("Perimeter:", self.get_perimeter(), "\n")


def main():
    # instantiate two rectangle objects
    r1 = Rectangle(4, 40)
    r2 = Rectangle(3.5, 35.7)
    # display the attributes
    print("Rectangle 1:")
    r1.display()
    print("Rectangle 2:")
    r2.display()

main()

'''
Rectangle 1:
Width: 4
Height: 40
Area: 160
Perimeter: 88

Rectangle 2:
Width: 3.5
Height: 35.7
Area: 124.95
Perimeter: 78.4
'''
