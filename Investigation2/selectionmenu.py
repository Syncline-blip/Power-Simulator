# Initial version of selectionmenu.py
# Exports user prompt and prints available houase appliances


def select():
    print('\n[ POWER MODELLER PROGRAM ]\n')
    print('\n[ PLEASE CHOOSE FROM APPLIANCES MENU (ENTER NAME): ]\n')
    inp = input(
        '[Appliance 1]:TV_Living\n[Appliance 2]:Fridge\n[Appliance 3]:Oven\n[Appliance 4]:Washing Machine\n[Appliance 5]:Microwave\n[Appliance 6]:Dryer\n[Appliance 7]:Hairdryer\n[Appliance 8]:Study Lamp\n[Appliance 9]:Computer\n[Appliance 10]:Laptop: ')
    return inp