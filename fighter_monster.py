from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    def __str__(self):
        return f"{self.name}, возраст: {self.age}"

    def __repr__(self):
        return self.__str__()

class Sword(Weapon):
    def attack(self):
        print(f"Боец наносит удар мечом.")
        print(f"Монстр побежден!")

class Bow(Weapon):
    def attack(self):
        print(f"Боец стреляет из лука.")
        print(f"Монстр побежден!")

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self):
        print(f"Боец {self.name} выбирает {self.weapon}")

    def fighter_attack(self):
        self.weapon.attack()


sword = Sword()
bow = Bow()
fighter = Fighter("Peter", Sword())
fighter.change_weapon()
fighter.fighter_attack()