class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
    

    def dead(num):
        Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(cls):
        print(f'태어난 개 {cls.birth_of_dogs}마리, 개는 총 {cls.num_of_dogs} 마리')

    def bark(cls):
        print("왈!")

Choco = Doggy('초코', '말티즈')
Choco.get_status()
Choco.bark()
print(Doggy.num_of_dogs)
print(Choco.name)
print(Choco.breed)
    