# Write your code here
import random


def generateCardNumber():
    iin = '400000'
    random_num = random.randint(1000, 9999)
    random_num = str(random_num).zfill(4)
    random_num2 = random.randint(1000, 9999)
    random_num2 = str(random_num2).zfill(4)
    random_num3 = random.randint(10, 99)
    random_num3 = str(random_num3).zfill(2)
    return int(iin + random_num + random_num2 + random_num3)


def generatePin():
    random_pin = random.randint(1000, 9999)
    random_pin = str(random_pin).zfill(4)
    return int(random_pin)


class BankUser:
    data = {}

    def __init__(self):
        self.card_number = generateCardNumber()
        self.pin = generatePin()
        BankUser.data[self.pin] = self.card_number


BankSystem = BankUser()
show_menu = True
while show_menu:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    menu_case = int(input())
    print()
    if menu_case == 1:
        print("Your card has been created")
        new_user = BankUser()
        print("Your card number:")
        print(new_user.card_number)
        print("Your card PIN:")
        print(new_user.pin)
        print()
    elif menu_case == 2:
        print("Enter your card number:")
        user_number = int(input())
        print("Enter your PIN:")
        user_pin = int(input())
        print()
        if BankSystem.data.get(user_pin) == user_number:
            print("You have successfully logged in!\n")
            show_menu2 = True
            while show_menu2:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                menu_case2 = int(input())
                print()
                if menu_case2 == 1:
                    print("Balance: 0\n")
                elif menu_case2 == 2:
                    print("You have successfully logged out!\n")
                    show_menu2 = False
                elif menu_case2 == 0:
                    show_menu2 = False
                    show_menu = False
        else:
            print("Wrong card number or PIN\n")
    elif menu_case == 0:
        print("Bye!")
        show_menu = False
