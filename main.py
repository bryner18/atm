import sys
from random import randint


def main():
    atm_login()


def atm_login():
    print("****************Welcome to ATM 24 hours******************")
    login_attempts = 3
    while login_attempts > 0:
        login_identifier = input("Type your user: ")
        if login_identifier == open("user_identifier.txt").read():
            login_pin = input("Type your PIN: ")
            if login_pin == open("user_pin.txt").read():
                print("Thanks for login!")
                return atm_main_menu()
            else:
                print("Sorry, your PIN is incorrect")
                login_attempts = login_attempts - 1
        else:
            print("Sorry, your user is incorrect")
            login_attempts = login_attempts - 1
    print("Sorry, you already tried 3 times!")


def atm_main_menu():
    print("****************Welcome to ATM 24 hours******************")
    print("Choose your option: ")
    print("1. Retire")
    print("2. Consult")
    print("3. Deposit")
    print("4. Phone recharge")
    print("5. Exit")
    user_choice = (input("Your choice: "))
    if user_choice == "1":
        return atm_retire()
    elif user_choice == "2":
        return atm_consult()
    elif user_choice == "3":
        return atm_deposit()
    elif user_choice == "4":
        return atm_recharge()
    elif user_choice == "5":
        return sys.exit()


def atm_retire():
    retire = input("Type the amount to retire: ")
    for line in open("user_money.txt"):
        if line.strip():
            user_money = int(line)
    if int(retire) > user_money:
        print("Sorry, you don't have sufficient money")
    else:
        for line in open("user_money.txt"):
            if line.strip():
                user_money_int = int(line)
                updated_balance = user_money_int - int(retire)
                print("Thank you,", retire, "was retired from your account")
                user_money_file = open("user_money.txt", "w")
                user_money_file.write(str(updated_balance))
                user_money_file.close()

                print("Go to main menu\n1. Yes\n2. No")
                decision = input("Decision: ")
                if decision == "1":
                    return atm_main_menu()
                elif decision == "2":
                    sys.exit()
                elif decision != "1" and decision != "2":
                    print("Sorry, incorrect option")


def atm_consult():
    print("Your current balance is:", open("user_money.txt").read(), "dollars")

    print("Go to main menu\n1. Yes\n2. No")
    decision = input("Decision: ")
    if decision == "1":
        return atm_main_menu()
    elif decision == "2":
        sys.exit()
    elif decision != "1" and decision != "2":
        print("Sorry, incorrect option")


def atm_deposit():
    deposit = input("Type the amount you want to deposit: ")
    for line in open("user_money.txt"):
        if line.strip():
            user_money_int = int(line)
            updated_balance = user_money_int + int(deposit)
            print("Thank you,", deposit, "was deposited in your account")
            user_money_file = open("user_money.txt", "w")
            user_money_file.write(str(updated_balance))
            user_money_file.close()

            print("Go to main menu\n1. Yes\n2. No")
            decision = input("Decision: ")
            if decision == "1":
                return atm_main_menu()
            elif decision == "2":
                sys.exit()
            elif decision != "1" and decision != "2":
                print("Sorry, incorrect option")


def atm_recharge():
    print("Select your carrier:\n1. Altice\n2. Claro\n3. Viva")
    user_decision = input("Decision: ")

    if user_decision == "1":
        recharge_amount = input("Type the recharge amount: ")
        print("Thank you,", recharge_amount, "were removed from your account.")
        print("Here is your recharge code:", randint(10000, 99999))
        for line in open("user_money.txt"):
            if line.strip():
                user_money_int = int(line)
                updated_balance = user_money_int - int(recharge_amount)
                user_money_file = open("user_money.txt", "w")
                user_money_file.write(str(updated_balance))
                user_money_file.close()

                print("Go to main menu\n1. Yes\n2. No")
                decision = input("Decision: ")
                if decision == "1":
                    return atm_main_menu()
                elif decision == "2":
                    sys.exit()
                elif decision != "1" and decision != "2":
                    print("Sorry, incorrect option")

    elif user_decision == "2":
        recharge_amount = input("Type the recharge amount: ")
        print("Thank you,", recharge_amount, "were removed from your account.")
        print("Here is your recharge code:", randint(10000, 99999))
        for line in open("user_money.txt"):
            if line.strip():
                user_money_int = int(line)
                updated_balance = user_money_int - int(recharge_amount)
                user_money_file = open("user_money.txt", "w")
                user_money_file.write(str(updated_balance))
                user_money_file.close()

                print("Go to main menu\n1. Yes\n2. No")
                decision = input("Decision: ")
                if decision == "1":
                    return atm_main_menu()
                elif decision == "2":
                    sys.exit()
                elif decision != "1" and decision != "2":
                    print("Sorry, incorrect option")

    elif user_decision == "3":
        recharge_amount = input("Type the recharge amount: ")
        print("Thank you,", recharge_amount, "were removed from your account.")
        print("Here is your recharge code:", randint(10000, 99999))
        for line in open("user_money.txt"):
            if line.strip():
                user_money_int = int(line)
                updated_balance = user_money_int - int(recharge_amount)
                user_money_file = open("user_money.txt", "w")
                user_money_file.write(str(updated_balance))
                user_money_file.close()

                print("Go to main menu\n1. Yes\n2. No")
                decision = input("Decision: ")
                if decision == "1":
                    return atm_main_menu()
                elif decision == "2":
                    sys.exit()
                elif decision != "1" and decision != "2":
                    print("Sorry, incorrect option")


main()