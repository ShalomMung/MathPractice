from math import pi, sqrt

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 4*pi*self.radius**2
    
    @property
    def volume(self):
        return (self.area*self.radius**3)/3

    @classmethod
    def from_volume(cls, volume):
        radius = (3*volume/(4*pi)) ** (1/3)
        return cls(radius)

if __name__ == "__main__":
    s = Sphere(3)
    print(f"Area of sphere: {s.area:.2f}")
    print(f"Volume of sphere: {s.volume:.2f}")
    #print(f"Volume of sphere: {s.from_volume(113):.2f}")
    #print(s.from_area(10))
    #print(s.area)