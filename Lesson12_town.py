import random


class Street:
    def __init__(self, name):
        self.name = name


class Town:
    def __init__(self, streets):
        self.streets = streets

    def pr_s(self):
        print(self.streets)


class House:
    def __init__(self, house):
        pass


Town1 = Town([Street(f"Будинок_{i}") for i in range(random.randrange(3))])
Town1.pr_s()
