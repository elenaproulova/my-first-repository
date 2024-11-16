
class Store():
    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items

    def add_item(self):
        key = str(input(f"Введите новое наименование товара для магазина {self.name}: "))
        value = float(input("Введите стоимость: "))
        self.items[key] = value
        print(f"В магазине {self.name} есть {self.items}")

    def delete_item(self):
        key = str(input(f"Введите товар, который надо удалить в магазине {self.name}: "))
        if key in self.items:
            del self.items[key]
            print(f"Ассортимент магазина {self.name}: {self.items}")
        else:
            print(f"Такого товара нет в ассортименте магазина {self.name}")

    def call_item(self):
        key = str(input(f"Введите товар, который надо найти в магазине {self.name}: "))
        self.items.get(key)
        print(f"{key} стоит {self.items.get(key)}")

    def update_item(self):
        key = str(input(f"Введите наименование товара для обновления в магазине {self.name}: "))
        value = float(input("Введите стоимость: "))
        if key in self.items:
            self.items[key] = value
            print(f"Ассортимент магазина: {self.items}")
        else:
            print(f"Такого товара нет в ассортименте")

shop1 = Store(name="Продукты", address="ул.Победы,7", items={
    "яблоки":120,
    "молоко":59,
    "хлеб":35
})
shop2 = Store(name="Игрушки", address="ул.Ленина,12", items={
    'кран':69,
    'ведро':15,
    'кукла':33
})
shop3 = Store(name="Хозтовары", address="ул.Луначарского,25", items={
    'порошок':55,
    'мыло':22,
    'паста':45
})

shop2.add_item()
shop1.call_item()
shop1.delete_item()
shop3.add_item()
shop3.add_item()
shop3.update_item()
print(shop1.items)
print(shop2.items)
print(shop3.items)

