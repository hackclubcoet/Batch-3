# SAMYUKTHA_P 3 TO MAKE A COFFEE MACHINE SYSTEM
money = 0
water = 700
milk = 850
beans = 190
cups = 20
selected_cups = 1


class ResourceError(Exception):  # CLASS IS A CODE TEMPLATE FOR CREATING OBJECTS.
    pass  # NULL STATEMENT.


print("HEY FRIEND!!")


def select_action() -> str:  # SELECT_ACTION DEFINES THE RETURN INPUT BELOW.
    return input("SELECT ACTION (buy, fill, take, exit): ")  # RETURNS THE RESULT.


def select_flavor() -> int:  # SELECT_FLAVOR DEFINES THE RESPONSE OF THE USER.
    print()
    response = input("What kind of COFFEE do you want to buy?\n"
                     " 1 - Espresso\n"
                     " 2 - Latte\n"
                     " 3 - Cappuccino\n"
                     " 4 - Doppio\n"
                     " 5 - Flat white\n"
                     " 6 - Black\n"
                     " 7 - Americano\n"
                     " 8 - Galao\n"
                     " back - to main menu: ")
    if response == "back":
        return 0
    return int(response)


def is_enough(needed_water=0, needed_milk=0, needed_beans=0, needed_cups=0):
    if water < needed_water & milk < needed_milk & beans < needed_beans & cups < needed_cups:
        print(" Uh-oh!, not enough resources for a drink, Sorry\n")
        raise ResourceError  # RAISE AN EXCEPTION WHEN DETECTING AN ERROR.
    else:
        print("I have enough resources, The coffee is coming!!\n")


# IS_ENOUGH DEFINES THE SUFFICIENT RESOURCES REQUIRED. IF THERE ARE ENOUGH RESOURCES,
# THE SECOND PRINT STATEMENT IS EXECUTED, OTHERWISE THE FIRST.

def buy():  # DEFINES THE THING TO BE BOUGHT.
    global money, water, milk, beans, cups
    flavor = select_flavor()

    try:  # TRY THE GIVEN CLAUSE IN BETWEEN TRY AND EXCEPT.
        if flavor == 0:
            pass
        elif flavor == 1:  # ESPRESSO
            is_enough(needed_water=250, needed_beans=16)

            money = 4
            water -= 250
            beans -= 16
            cups -= 1
        elif flavor == 2:  # LATTE
            is_enough(needed_water=350, needed_milk=75, needed_beans=20)

            money = 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavor == 3:  # CAPPUCCINO
            is_enough(needed_water=200, needed_milk=100, needed_beans=12)

            money = 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        elif flavor == 4:  # DOPPIO
            is_enough(needed_water=300, needed_beans=20)

            money = 8
            water -= 300
            beans -= 20
            cups -= 1
        elif flavor == 5:  # FLAT WHITE
            is_enough(needed_water=200, needed_milk=100, needed_beans=16)

            money = 8
            water -= 200
            milk -= 100
            beans -= 16
            cups -= 1
        elif flavor == 6:  # BLACK
            is_enough(needed_water=200, needed_beans=12)

            money = 2
            water -= 200
            beans -= 12
            cups -= 1
        elif flavor == 7:  # AMERICANO
            is_enough(needed_water=200, needed_beans=14)

            money = 4
            water -= 200
            beans -= 14
            cups -= 1
        elif flavor == 8:  # GALAO
            is_enough(needed_water=200, needed_milk=200, needed_beans=16)

            money = 8
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:  # IF EXCEPTION, THE REST OF THE CLAUSE IS SKIPPED.
        pass


# THE IF AND ELIF STATEMENTS HELP TO SELECT THE COFFEE FLAVOR.
# ELSE, RAISE AN ERROR WITH A MESSAGE.

def fill():  # DEFINES HOW MANY CUPS TO BE FILLED.
    global selected_cups

    print()
    selected_cups = int(input("How many disposable cups of coffee"
                              " do you want to add: "))
    print()


def take():  # DEFINES THE COST OF EACH CUP OF COFFEE.
    global money, selected_cups

    print()
    print(f'You should give me ${money * selected_cups}')
    print()

    money = 0


def exit():  # DEFINES EXIT FROM THE PROGRAM AND PRINTS A MESSAGE.
    print("BYE.....HAVE A GOOD DAY!!")


def main():  # ENTRY OF THE PROGRAM
    while True:  # TO SELECT THE REQUIRED ACTION BY THE USER EACH TIME.
        action = select_action()

        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "exit":
            exit()
            break  # TO EXIT THE LOOP
        else:
            raise ResourceError(f'Unknown command {action}')


# IF AND ELIF STATEMENTS HELP TO SELECT THE REQUIRED ACTION.
# ELSE RAISE AN ERROR WITH A MESSAGE.

if __name__ == '__main__':
    main()
