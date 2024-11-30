from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

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

    def choose_weapon(self):
        print(f"Боец {self.name} выбирает {self.weapon}")

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"Боец {self.name} выбирает {self.weapon}")

    def fighter_attack(self):
        self.weapon.attack()


sword = Sword()
bow = Bow()
fighter = Fighter("Peter", sword)
fighter.choose_weapon()
fighter.fighter_attack()
fighter.change_weapon(bow)
fighter.fighter_attack()
