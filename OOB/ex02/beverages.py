class HotBeverage:
    price = 0.30
    name = "hot beverage"
    description = "Just some hot water in a cup."
    def Description(self):
        return self.description
    def __str__(self):
        return "name : ", self.name, "\nprice: ", self.price, "\ndescription: ", self.description()

class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
        self.description = "A coffee, to stay awake."
    # price = 0.40
    # name = "coffee"
    # description = "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.price = 0.30
        self.name = "tea"
        self.description = "A tea, to relax."

class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
        self.description = "A chocolate, to sweeten your day."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"
        self.description = "Un po' di Italia in una tazza!"


if __name__ == "__main__":
    hot = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print(hot.Description())
    print(coffee.Description())
    print(tea.Description())
    print(chocolate.Description())
    print(cappuccino.Description())