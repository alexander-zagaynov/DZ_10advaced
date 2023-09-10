
class Animals:

    def __init__(self, name: str, age: int, say: str, eat: str):
        self.name = name
        self.age = age
        self.say = say
        self.eat = eat



    def say(self):
        pass

    def eat(self):
        return " делаю ням-ням"

    def __str__(self):
        return f"{self.name} {self.age} {self.say} {self.eat}"



class Fish(Animals):

    def __init__(self, name: str, age: int, say: str, eat: str):
        super().__init__(name, age, say, eat)

    def say(self):
        return ("кар-кар")

    def eat(self):
        return ("ням-ням")

    def __str__(self):
        return f"{super().__str__()}"



class Birds(Animals):

    def __init__(self, name: str, age: int,  say: str, eat: str):

        super().__init__(name, age, say, eat)

    def say(self):
        return ("чик-чирик")

    def eat(self):
        return ("ням-ням")

    def __str__(self):
        return f"{super().__str__()} "


if __name__ == '__main__':
    fish1 = Fish("карп", 2, "говорю буль-буль", " делаю ням-ням")
    bird1 = Birds("воробей", 2, "чик-чирик", "делаю ням-ням")
    print(fish1)
    print(bird1)

