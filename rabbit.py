
class Rabbit:
    nr_rabbit = 0
    rabbits = []

    def __init__(self):
        Rabbit.nr_rabbit += 1
        Rabbit.rabbits.append(self)
    
    def __repr__(self):
        return self.__class__.__name__

def main():

    r1 = Rabbit()
    r2 = Rabbit()
    r3 = Rabbit()
    print("Number of rabbits = ", r2.nr_rabbit)
    print("Number of rabbits object = ", Rabbit.rabbits)
    
if __name__ == "__main__":
    main()