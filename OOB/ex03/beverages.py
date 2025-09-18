class HotBeverage:
    price = 0.30
    name = "hot beverage"
    description = "Just some hot water in a cup."
    def Description(self):
        return self.description
    def __str__(self):
         return (
        "name: " + str(self.name) + 
        "\nprice: " + str(self.price) + 
        "\ndescription: " + str(self.Description())
    )

class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"
    description = "A coffee, to stay awake."


class Tea(HotBeverage):
    price = 0.30
    name = "tea"
    description = "Just some hot water in a cup."

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    description = "Un po' di Italia in una tazza!"


# if __name__ == "__main__":
#     hot = HotBeverage()
#     coffee = Coffee()
#     tea = Tea()
#     chocolate = Chocolate()
#     cappuccino = Cappuccino()
#     print(hot.Description())
#     print(coffee.Description())
#     print(tea.Description())
#     print(chocolate.Description())
#     print(cappuccino.Description())