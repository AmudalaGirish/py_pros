class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f"{self.color} {self.name}"

class Veg:
    def __init__(self, name, color):
        self.name = name
        self.color = color

apple = Fruit("apple", "RED")
banana = Fruit("banana", "YEllOW")
carrot = Veg("carort", "ORAGE")

print(apple)
print(banana)
print(carrot)
