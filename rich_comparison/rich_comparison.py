class Cat:

    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def __eq__(self, other):
        if hasattr(other, 'age'):
            return self.weight == other.weight
        else:
            raise TypeError

    def __lt__(self, other):
        if hasattr(other, 'age'):
            return self.weight < other.weight
        else:
            raise TypeError

    def __le__(self, other):
        if hasattr(other, 'age'):
            return self.weight <= other.weight
        else:
            raise TypeError

    def __ne__(self, other):
        if hasattr(other, 'age'):
            return self.weight != other.weight
        else:
            raise TypeError

    def __gt__(self, other):
        if hasattr(other, 'age'):
            return self.weight > other.weight
        else:
            raise TypeError

    def __ge__(self, other):
        if hasattr(other, 'age'):
            return self.weight >= other.weight
        else:
            raise TypeError


class Dog:

    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def __eq__(self, other):
        if hasattr(other, 'age'):
            return self.age == other.age
        else:
            raise TypeError

    def __lt__(self, other):
        if hasattr(other, 'age'):
            return self.age < other.age
        else:
            raise TypeError

    def __le__(self, other):
        if hasattr(other, 'age'):
            return self.age <= other.age
        else:
            raise TypeError

    def __ne__(self, other):
        if hasattr(other, 'age'):
            return self.age != other.age
        else:
            raise TypeError

    def __gt__(self, other):
        if hasattr(other, 'age'):
            return self.age > other.age
        else:
            raise TypeError

    def __ge__(self, other):
        if hasattr(other, 'age'):
            return self.age >= other.age
        else:
            raise TypeError


if __name__ == '__main__':
    murka = Cat('Murka', 19, 4, 'kalico')
    lapa = Cat('Lapa', 7, 6, 'black')
    alice = Cat('Alice', 12, 10, 'white')
    barbos = Dog('Barbos', 2, 10, 'black')
    tuzik = Dog('Tuzik', 13, 18, 'white')
    bobik = Dog('Bobik', 13, 10, 'ginger')
    dusya = Dog('Dusya', 8, 12, 'orange')

    print(tuzik == murka)
    print(barbos < bobik)
    print(tuzik < dusya)
    print(tuzik < murka)
    print(tuzik == bobik)
    print(lapa > murka)
    print(dusya < alice)
    print(lapa != bobik)
