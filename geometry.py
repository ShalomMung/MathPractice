
class Geometry:
    @classmethod
    def unit(cls):
        return cls(1)
    
class Sphere(Geometry):
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"{self.__class__.__name__}{self.radius}"
        
class Circle(Geometry):
    def __init__(self, radius):
        self.radius = radius
    
    def __repr__(self):
        return f"{self.__class__.__name__}{self.radius}"
    
def main():
    s = Sphere.unit()
    c = Circle.unit()
    print(s, c)

if __name__ == "__main__":
    main()