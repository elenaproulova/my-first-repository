class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук")

    def eat (self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)

    def make_sound(self):
        print(f"{self.name} щебечет")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} кричит")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} шипит")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print("added")

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_animal(self):
        print(f"список животных {self.animals}")

    def list_employee(self):
        print(f"список сотрудников {self.employees}")

    def file_list(self):
        with open("zoo_list.txt", "w", encoding='utf-8') as file:
            file.write(str(self.animals))
        with open("zoo_list.txt", "a") as file:
            file.write(str(self.employees))

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self,):
        print(f"{self.name} работает")

class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self,):
        print(f"{self.name} кормит животных")

class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    def work(self,):
        print(f"{self.name} лечит животных")


bird1 = Bird("Птица", 2)
dog = Mammal("Собака", 3)
snake = Reptile("Змея", 1)
keeper1 = ZooKeeper("Иван", 50)
veterin1 = Veterinarian("Сергей", 43)

bird1.make_sound()
dog.make_sound()
snake.make_sound()
keeper1.work()
veterin1.work()
animals1 = Zoo()
employees1 = Zoo()
animals1.add_animal(bird1)
animals1.add_animal(dog)
animals1.add_animal(snake)
animals1.list_animal()
employees1.add_employee(veterin1)
employees1.add_employee(keeper1)
employees1.list_employee()
animals1.file_list()
employees1.file_list()




