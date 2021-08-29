# Написать программу Город.
# Создать три отдельных объекта: City, Street, House.
# У города должны быть улицы (City -> [Street]), у улиц должны быть дома Street -> [House].
# У города есть улицы и дома и возможности их добавлять и удалять.
#   Улицы могут вместить случайное количество домов от 5 до 20.
#   Дома могут иметь случайное количество населения от 1 до 100.
#   Должна быть возможность наполнить город одним методом.
#   У города должен быть метод который вернет количество населения.
#   *доп. Написать метод который сможет напечатать таблицей:
# Улица Дом Население
#   1   1         5
#   1   2         10
#   1   3         25
#                 и т.д.

from random import randint


class City:
    def __init__(self):
        self.streets = []

    def generate(self):
        for i in range(randint(1, 100)):
            self.streets.append(Street(i))

    @property
    def population(self):
        with open('population.txt', 'w') as file:
            population = 0
            file.write(f'Street \t House \t Population\n')
            for street in self.streets:
                for house in street.houses:
                    file.write(f'{street.number: <5}\t {house.number: <5}\t {house.humans}\n')
                    population += house.humans
        return f'Total population - {population} people.'


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []
        self.generate()

    def generate(self):
        for i in range(randint(5, 20)):
            self.houses.append(House(i))


class House:
    def __init__(self, number):
        self.number = number
        self.humans = randint(1, 100)


test = City()
test.generate()
print(test.population)
