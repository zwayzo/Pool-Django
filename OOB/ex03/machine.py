import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self, name):
        self.name = name
        self.coin = 10
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
            self.description = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.coin = 10
        print("The machine has been repaired.")

    
    def serve(self, Tea):
        if self.coin <= 0:
            raise self.BrokenMachineException()
        self.coin -= 1
        if random.randint(1, 10) % 2 == 1:
            return Tea()
        return self.EmptyCup()


if __name__ == "__main__":
    # choices = [coffee, tea, /chocolate, cappuccino]
    coffee_machine = CoffeeMachine("Coffee-matic")
    
    for i in range (22):
        try:
            print("\n\n",coffee_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()
            


   


