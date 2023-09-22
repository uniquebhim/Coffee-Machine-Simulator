from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# resources=MenuItem()
items=Menu()
material=CoffeeMaker()
money=MoneyMachine()


def Coffee_Machine():
    should_continue=True
    while should_continue:
        Choice=input(f"What would you like? ({items.get_items()}) :").lower()
        if Choice=="off":
            should_continue=False
            quit()
        elif Choice=="report":
            material.report()
            money.report()
        else:
            if material.is_resource_sufficient(items.find_drink(Choice)):
                if money.make_payment(items.find_drink(Choice).cost):
                    material.make_coffee(items.find_drink(Choice))
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(
                    "Sorry We do not have sufficient material to make your {Choice} Coffee")

        




Coffee_Machine()