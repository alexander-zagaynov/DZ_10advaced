from factory import Animals, Fish, Birds


class Factory(Birds, Fish, Animals):

    @staticmethod
    def create_animal(name: str, age: int, say: str, eat: str):
        return Animals(name, age, say, eat)

    @staticmethod
    def create_fish(name: str, age: int, say: str, eat: str):
        return Fish(name, age, say, eat)

    @staticmethod
    def create_bird(name: str, age: int,  say: str, eat: str):
        return Birds(name, age, say, eat)


if __name__ == '__main__':
    any_animal = Factory.create_animal('Медведь', 500, 'рррррр', 'хрум-хрум')
    print(any_animal)
    raven = Factory.create_bird('Ворона', 2, 'кар', 'тук- тук')
    print(raven)
    shark = Factory.create_fish('Акула', 300, ' брррр', 'хрям')
    print(shark)
