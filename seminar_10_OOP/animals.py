''' Задача 5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.'''

''' Задача 6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.'''


class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Bird(Animal):
    def __init__(self, bird_type: str, singing: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bird_type = bird_type
        self.sound = singing

    def __str__(self):
        return f"{super().__str__()} {self.bird_type} {self.sound}"


class Dog(Animal):
    def __init__(self, breed: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()} {self.breed}"


class Fish(Animal):
    def __init__(self, fish_type: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fish_type = fish_type

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


if __name__ == '__main__':
    print(Dog("Такса", "Рэкс", 40, 5))
    print(Bird("Parrot", "Чирик","Гоша", 1, 3))
    print(Fish("Regal_blue", "Dory", 10, 5))
