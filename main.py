import sys
from random import randint


login_identifier = input("Type your user: ")
login_pin = input("Type your pin: ")


class getToken:

    def __init__(self, login_identifier, login_pin):
        self.login_identifier = login_identifier
        self.login_pin = login_pin

    def __getToken__(self):
        userToken = 0
        login_identifier_file = open("user_identifier.txt", "r")
        x = login_identifier_file.read().splitlines()
        if login_identifier in x:
            userToken = x.index(login_identifier)
        else:
            print("Sorry, we couldn't find your user")
            sys.exit()

        loginToken = 0
        login_pin_file = open("user_pin.txt", "r")
        x = login_pin_file.read().splitlines()
        if login_pin in x:
            loginToken = x.index(login_pin)
        else:
            print("Sorry, we couldn't find your password")
            sys.exit()

        if userToken == loginToken:
            print("You've logged in,", login_identifier)
            login_identifier_file.close()
            login_pin_file.close()
            return userToken
        else:
            print("Sorry, your user / pin are incorrect.")
            sys.exit()


inst = getToken(login_identifier, login_pin)
userToken = inst.__getToken__()

loop = 1
while loop == 1:
    print("----------------------------------------------------\n"
          "|             Welcome to ATM 24 HOURS              |\n"
          "----------------------------------------------------")
    print("Choose your option: ")
    print("1. Retire")
    print("2. Consult")
    print("3. Deposit")
    print("4. Phone recharge")
    print("5. Exit")
    user_choice = (input("Your choice: "))
    if user_choice == "1":
        retire = input("Type the amount to retire: ")
        user_money_file = open("user_money.txt", "r")
        money_list = user_money_file.readlines()
        user_money = int(money_list[userToken])
        if user_money > int(retire):
            print("You can complete the transaction!")
            updated_balance = str(int(user_money) - int(retire))

            money_list = []
            with open("user_money.txt", "r") as f:
                get_all = f.readlines()
                for x in get_all:
                    money_list.append(x)
            money_list[userToken] = (updated_balance + "\n")

            file = open("user_money.txt", "w")
            for line in money_list:
                file.write(line)
            file.close()

            print("Would you like to continue to the main menu?\n1. Yes\n2. No")
            choice = int(input("Decision: "))
            if choice != 1:
                print("Thank you for coming,", login_identifier)
                sys.exit()
            else:
                loop = 1

    elif user_choice == "2":
        money_list = []
        with open("user_money.txt", "r") as f:
            get_all = f.readlines()
            for x in get_all:
                money_list.append(x)
        print("Your current balance is:", money_list[userToken])

        print("Would you like to continue to the main menu?\n1. Yes\n2. No")
        choice = int(input("Decision: "))
        if choice != 1:
            print("Thank you for coming,", login_identifier)
            sys.exit()
        else:
            loop = 1

    elif user_choice == "3":
        deposit = int(input("Write the amount you want to deposit: "))

        user_money_file = open("user_money.txt", "r")
        money_list = user_money_file.readlines()
        user_money = int(money_list[userToken])
        updated_balance = str(int(user_money) + int(deposit))

        money_list = []
        with open("user_money.txt", "r") as f:
            get_all = f.readlines()
            for x in get_all:
                money_list.append(x)
        money_list[userToken] = (updated_balance + "\n")

        file = open("user_money.txt", "w")
        for line in money_list:
            file.write(line)
        file.close()

        print("Would you like to continue to the main menu?\n1. Yes\n2. No")
        choice = int(input("Decision: "))
        if choice != 1:
            print("Thank you for coming,", login_identifier)
            sys.exit()
        else:
            loop = 1

    elif user_choice == "4":
        print("Please select the carrier:\n1. Altice\n2. Claro\n3. Viva")
        decision = int(input("Decision: "))
        amount = int(input("Type the amount of the recharge: "))
        if decision == 1:
            print("You selected the carrier Altice")
            user_money_file = open("user_money.txt", "r")
            money_list = user_money_file.readlines()
            user_money = int(money_list[userToken])
            updated_balance = str(int(user_money) - int(amount))

            money_list = []
            with open("user_money.txt", "r") as f:
                get_all = f.readlines()
                for x in get_all:
                    money_list.append(x)
            money_list[userToken] = (updated_balance + "\n")

            file = open("user_money.txt", "w")
            for line in money_list:
                file.write(line)
            file.close()

            print("Here is your code:", randint(10000, 99999))

            print("Would you like to continue to the main menu?\n1. Yes\n2. No")
            choice = int(input("Decision: "))
            if choice != 1:
                print("Thank you for coming,", login_identifier)
                sys.exit()
            else:
                loop = 1

        elif decision == 2:
            print("You selected the carrier Claro")
            user_money_file = open("user_money.txt", "r")
            money_list = user_money_file.readlines()
            user_money = int(money_list[userToken])
            updated_balance = str(int(user_money) - int(amount))

            money_list = []
            with open("user_money.txt", "r") as f:
                get_all = f.readlines()
                for x in get_all:
                    money_list.append(x)
            money_list[userToken] = (updated_balance + "\n")

            file = open("user_money.txt", "w")
            for line in money_list:
                file.write(line)
            file.close()

            print("Here is your code:", randint(10000, 99999))

            print("Would you like to continue to the main menu?\n1. Yes\n2. No")
            choice = int(input("Decision: "))
            if choice != 1:
                print("Thank you for coming,", login_identifier)
                sys.exit()
            else:
                loop = 1

        elif decision == 3:
            print("You selected the carrier Viva")
            user_money_file = open("user_money.txt", "r")
            money_list = user_money_file.readlines()
            user_money = int(money_list[userToken])
            updated_balance = str(int(user_money) - int(amount))

            money_list = []
            with open("user_money.txt", "r") as f:
                get_all = f.readlines()
                for x in get_all:
                    money_list.append(x)
            money_list[userToken] = (updated_balance + "\n")

            file = open("user_money.txt", "w")
            for line in money_list:
                file.write(line)
            file.close()

            print("Here is your code:", randint(10000, 99999))

            print("Would you like to continue to the main menu?\n1. Yes\n2. No")
            choice = int(input("Decision: "))
            if choice != 1:
                print("Thank you for coming,", login_identifier)
                sys.exit()
            else:
                loop = 1

    elif user_choice == "5":
        print("Thank you for coming,", login_identifier)
        sys.exit()
