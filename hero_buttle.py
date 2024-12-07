class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f"{self.name} атакует")
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game():
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero('Компьютер')

    def start(self):
        print("Игра началась")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

player_name = input("Ведите имя игрока")
game = Game(player_name)
game.start()