# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

class CoffeeMachine():

    def __init__(self):
        self.avail_water = 400
        self.avail_milk = 540
        self.avail_beans = 120
        self.avail_cups = 9
        self.avail_money = 550

    def available(self):
        print("The coffee machine has:")
        print(self.avail_water, "of water")
        print(self.avail_milk, "of milk")
        print(self.avail_beans, "of coffee beans")
        print(self.avail_cups, "of disposable cups")
        print(self.avail_money, "of money")

    def if_possible(self, item):
        if self.item == "1":
            if self.avail_water < 250:
                print("Sorry, not enough water!")
                print()
            elif self.avail_beans < 16:
                print("Sorry, not enough coffee beans!")
                print()
            elif self.avail_cups < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                return True
        elif self.item == "2":
            if self.avail_water < 350:
                print("Sorry, not enough water!")
                print()
            elif self.avail_milk < 75:
                print("Sorry, not enough milk!")
                print()
            elif self.avail_beans < 20:
                print("Sorry, not enough coffee beans!")
                print()
            elif self.avail_cups < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                return True
        if self.item == "3":
            if self.avail_water < 200:
                print("Sorry, not enough water!")
                print()
            elif self.avail_milk < 100:
                print("Sorry, not enough milk!")
                print()
            elif self.avail_beans < 12:
                print("Sorry, not enough coffee beans!")
                print()
            elif self.avail_cups < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                return True

    def buy(self):
        self.item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if self.if_possible(self.item) == True:
            print("I have enough resources, making you a coffee!")
            print()
            if self.item == "1":
                self.avail_water -= 250
                self.avail_beans -= 16
                self.avail_cups -= 1
                self.avail_money += 4
            elif self.item == "2":
                self.avail_water -= 350
                self.avail_milk -= 75
                self.avail_beans -= 20
                self.avail_cups -= 1
                self.avail_money += 7
            else:
                self.avail_water -= 200
                self.avail_milk -= 100
                self.avail_beans -= 12
                self.avail_cups -= 1
                self.avail_money += 6

    def fill(self):
        self.avail_water += int(input("Write how many ml of water do you want to add: "))
        self.avail_milk += int(input("Write how many ml of milk do you want to add: "))
        self.avail_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.avail_cups += int(input("Write how many disposable cups of coffee do you want to add: "))


    def take(self):
        print("I gave you $" + str(self.avail_money))
        self.avail_money = 0

    def start(self):
        while True:
            self.action = input("Write action (buy, fill, take, exit, remaining): ")
            print()
            if self.action == "buy":
                self.buy()
            elif self.action == "fill":
                self.fill()
            elif self.action == "take":
                self.take()
            elif self.action == "exit":
                break
            else:
                self.available()

new = CoffeeMachine()
new.start()
