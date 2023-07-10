''' Домашнее задание
Доработаем задачи 5-6 (animals.py). Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.'''

from animals import Dog, Bird, Fish


class Creator():
  
    def create_animal(class_animal, *args, **kwargs):
        return class_animal(*args, **kwargs)
    

if __name__ == '__main__':    
    first = Creator.create_animal(Fish,'Regal_blue','Dory', 30, 4)
    print(first)
    second = Creator.create_animal(Dog,'Alsation','Rex', 12, 5)
    print(second)
    gosha = Creator.create_animal(Bird,'Parrot', 'Чирик', 'Гоша', 1, 3)
    print(gosha)