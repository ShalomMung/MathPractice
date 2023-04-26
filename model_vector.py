
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

class ModelVector(Vector):

    def __init__(self, name, x, y, z):
        self.name = name
        super().__init__(x, y, z)

    def __add__(self, other):
        vector_sum = super().__add__(other)
        return ModelVector(f"{self.name} + {other.name}", vector_sum.x, vector_sum.y, vector_sum.z)


def test_model_vector():
    print("Processing ..")
    u = ModelVector("u", 1, 1, 1)
    v = ModelVector("v" ,1, 1, 1) 
    w = u + v
    assert w.name == "u + v"
    assert w.x == u.x + v.x
    assert w.y == u.y + v.y
    assert w.z == u.z + v.z 
    print("Green")  

if __name__ == "__main__":
    #v1 = Vector(1, 2, 3)
    #u1 = Vector(1, 1, 1)
    #print(v1 + u1)

    test_model_vector()