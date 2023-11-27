class Square:
    def __init__(self, side1):
        self.side1 = side1
        self.side2 = side1

    def get_area(self):
        return self.side1 * self.side2

    def __add__(self,other):
        return self.get_area()+other.get_area()


class Rectangle(Square):
    def __init__(self, side1, side2):
        super().__init__(side1)
        self.side2 = side2



if __name__ == "__main__":
    s = Square(5)
    r = Rectangle(8, 2)

    print(f"square area = {s.get_area()}")
    print(f"rectangle area = {r.get_area()}")
    print(f"aggregated area is: {s+r}")
