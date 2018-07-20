class Common:
    name = ''
    weight = 0
    represent = 'кто-то'
    sound = '...'

    def __init__(self, name):
        print()
        print('У нас есть', self.represent, name)
        self.name = name
        if isinstance(self, Animal):
            represent = 'животного'
        else:
            represent = 'птицы'
        weight = input('Укажите вес '+represent+': ')
        try:
            self.weight = int(weight)
        except TypeError:
            self.weight = 0

    def say(self):  # общий метод голоса животного или птицы
        print(self.represent, self.name, 'говорит', '"' + self.sound + '"')

    def feed(self, weight):  # 2. накормить
        self.weight += weight
        print(self.represent, self.name, 'теперь весит: ', self.weight)

    def do_what_you_can(self):  # общий метод вызова основного действия подкласса животного или птицы
        if isinstance(self, Cow):
            self.get_milk()
        elif isinstance(self, Goat):
            self.get_milk()
        elif isinstance(self, Sheep):
            self.get_wool()

    def __add__(self, other):
        result = 0
        if isinstance(self, Common):
            result += self.weight
        else:
            result += self
        if isinstance(other, Common):
            result += other.weight
        else:
            result += other
        return result


class Animal(Common):
    pass


class MilkAnimal(Animal):
    def get_milk(self):  # 2. подоить
        print(self.represent, self.name, 'дает нам молоко')


class WoolAnimal(Animal):
    def get_wool(self):  # 2. постричь
        print(self.represent, self.name, 'дает нам шерсть')


class Cow(MilkAnimal):
    represent = 'корова'  # 1. Корова
    sound = 'Муу'


class Goat(MilkAnimal):  # 1. Коза
    represent = 'коза'
    sound = 'Бее'


class Sheep(WoolAnimal):  # 1. Баран
    represent = 'баран'
    sound = 'Бее'


class Bird(Common):
    pass


class EggsBird(Bird):
    def get_eggs(self):  # 2. собрать яйца
        print(self.represent, self.name, 'дает нам яйца')


class Goose(EggsBird):  # 1. Гусь
    represent = 'гусь'
    sound = 'Га'


class Hen(EggsBird):  # 1. Курица
    represent = 'курица'
    sound = 'Ко'


class Duck(EggsBird):  # 1. Утка
    represent = 'гусь'
    sound = 'Кря'


def main():
    # животные

    animals = list()
    animals.append(Cow('Манька'))
    animals.append(Goat('Рога'))
    animals.append(Goat('Копыта'))
    animals.append(Sheep('Барашек'))
    animals.append(Sheep('Кудрявый'))

    print()
    print('Наши животные:')

    for animal in animals:
        animal.say()
        animal.do_what_you_can()

    # птицы

    birds = list()
    birds.append(Goose('Серый'))
    birds.append(Goose('Белый'))
    birds.append(Hen('Ко-ко'))
    birds.append(Hen('Кукареку'))
    birds.append(Duck('Кряква'))

    print()
    print('Наши птицы:')

    for bird in birds:
        bird.say()
        bird.do_what_you_can()

    print()
    print('Теперь их нужно их всех покормить.')
    weight = input('Укажите вес еды:')
    try:
        weight = int(weight)
    except TypeError:
        weight = 0

    animals_birds = animals + birds

    for someone in animals_birds:
        someone.feed(weight)

    print()
    print('Вычисляем общий вес животных и птиц, вычисляем самое тяжелое животное или птицу...')

    weight = 0
    max_weight = 0
    owner_of_max_weight = None
    for someone in animals_birds:
        weight = someone + weight
        if someone.weight > max_weight:
            max_weight = someone.weight
            owner_of_max_weight = someone

    print('Общий вес:', weight)
    print('Самый тяжелый(ая):', owner_of_max_weight.represent, owner_of_max_weight.name)

    print()
    print('Работа завершена')


main()
