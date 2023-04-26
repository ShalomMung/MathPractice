import datetime

class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    @staticmethod
    def calculate_age(year_born):
        return datetime.datetime.now().year - year_born
    
    @property
    def age(self):
        return Person.calculate_age(self.year_born)
    
if __name__ == "__main__":
    p = Person("Mung", 1984)
    print(p.age)