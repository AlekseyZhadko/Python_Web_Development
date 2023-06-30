# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animals:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Fish(Animals):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Swim"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


class Bird(Animals):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.sound = sound
        self.bird_type = bird_type

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type}"


class Dog(Animals):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type}"


class Fabric():
    def animal(self, animal_type: str, *args):
        new_animal = self._marker(animal_type)
        return new_animal(*args)

    def _marker(self, animal_type: str):
        types = {"dog": Dog, "fish": fish, "bird": bird}
        return types[animal_type.lower()]


if __name__ == '__main__':
    dog = Dog("Рэкс", 40, 5, "Такса")
    bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
    fish = Fish("Карп", 10, 5, "Речная")
    print(dog)
    print(bird)
    print(fish)
    fabric = Fabric()
    animal_1 = fabric.animal("dog", "Рэкс", 40, 5, "Такса")
    print(animal_1)
