import random
import os
import platform

##CLI leegmaken
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

##lijsten met letters, nummers en symbolen
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']
opgeslagen_wachtwoorden = {}
lijn = ("-" * 100)
def validatie_generator():
    while True:
        amount_char = int(input('Hoeveel karakters wil je dat je wachtwoord uit bestaat? 1-64: '))
        if 1 <= amount_char <= 64:
            return amount_char
        else:
            print(f'Je koos {amount_char}. Kies een waarde tussen 1 en 64.')

def generator():
    """Met deze functie kan de gebruiker een nieuw wachtwoord aanmaken"""
    password = []
    ##Ik heb dit later toegevoegd omdat ik het vragen naar letters, symbolen en nummers niet handig vond voor de UX
    char = validatie_generator()
    while True:
        letter = random.randint(1, char)
        symbol = random.randint(1, char)
        number = random.randint(1, char)
        if letter + symbol + number == char:
            break

    # letter = int(input('Hoeveel letters wil je in je wachtwoord?: '))
    for i in range(letter):
        password.append(random.choice(letters))
    # symbol = int(input('Hoeveel symbolen wil je in je wachtwoord?: '))
    for i in range(symbol):
        password.append(random.choice(symbols))
    # number = int(input('Hoeveel nummers wil je in je wachtwoord?: '))
    for i in range(number):
        password.append(random.choice(numbers))
    password_app_name = str(input('In welke app wil je dit wachtwoord gebruiken?: '))
    random.shuffle(password)
    joined = ("".join(password))
    clear_screen()
    return password_app_name.title(), joined

def menu():
    """Toont het hoofdmenu en laat de gebruiker een keuze maken."""
    choice = int(input(
        "Welkom bij de wachtwoordgenerator!\n"
        "Wat wil je doen?\n"
        "1. Een nieuw wachtwoord genereren\n"
        "2. Opgeslagen wachtwoorden bekijken\n"
        "3. Een wachtwoord opzoeken\n"
        "4. Een wachtwoord verwijderen\n"
        "5. Alle wachtwoorden verwijderen\n"
        "6. De applicatie afsluiten\n"
        "Maak een keuze (1-5): "
    ))
    return choice

def search_password():
    """Deze functie doorzoekt de lijst met opgeslagen wachtwoorden en toont het wachtwoord als het bestaat."""
    search = input("Voor welke applicatie zoek je het wachtwoord?")
    search = search.title()
    if search not in opgeslagen_wachtwoorden:
        print(f'"{search}" staat niet in je opgeslagen wachtwoorden.')
    else:
        print(f'Het wachtwoord voor "{search}" is: {opgeslagen_wachtwoorden[search]}')
    return

def pop_password():
    """Deze functie verwijdert een wachtwoord uit de lijst met opgeslagen wachtwoorden als het bestaat."""
    if not opgeslagen_wachtwoorden:
        print('Er zijn nog geen opgeslagen wachtwoorden.')
    else:
        list_passwords()
        which_item = int(input("Welk item wil je verwijderen?"))
        count_dict_length = len(opgeslagen_wachtwoorden)
        if which_item > count_dict_length:
            print(f'Je input was {which_item}, maar je lijst bevat maar {count_dict_length} entries')
        else:
            keys = list(opgeslagen_wachtwoorden.keys())
            key_to_remove = keys[which_item-1]
            print(f'"{key_to_remove}" is verwijdert uit je lijst met wachtwoorden!')
            opgeslagen_wachtwoorden.pop(key_to_remove)
            return
    # Dit stuk bovenstaande stuk heb ik later ge-refactored omdat ik het op de bovenstaande manier 'cleaner' vond.
    # Onderstaande regels zijn m'n O.G. code

    # which_item = which_item.title()
    # if which_item not in opgeslagen_wachtwoorden:
    #     print(f'"{which_item}" staat niet in je opgeslagen wachtwoorden.')
    # else:
    #     print(f'Het wachtwoord "{opgeslagen_wachtwoorden[which_item]}" voor "{which_item}" is succesvol verwijderd.')
    #     opgeslagen_wachtwoorden.pop(which_item)
    # return

def list_passwords():
    """Deze functie toont de lijst met opgeslagen wachtwoorden en de bijbehorende applicaties."""
    if not opgeslagen_wachtwoorden:
        print('Er zijn nog geen opgeslagen wachtwoorden.')
    else:
        print("Opgeslagen wachtwoorden:")
        for index, (key, value) in enumerate(opgeslagen_wachtwoorden.items(), start=1):
            print(f'{index}. App: "{key}" Wachtwoord: {value}')
    return

def new_entry():
    """Deze functie splitst de tupel en stopt de nieuwe entry in een woordenboek"""
    new = generator()
    key, value = new
    opgeslagen_wachtwoorden[key] = value
    print(f'Het wachtwoord voor de app "{key}" is: {value}')
    return

def reset_list():
    """Deze functie verwijdert alle opgeslagen wachtwoorden"""
    if not opgeslagen_wachtwoorden:
        print('Er zijn nog geen opgeslagen wachtwoorden.')
    else:
        list_passwords()
        delete_password = int(input('Weet je zeker dat je alle bovenstaande entries wil verwijderen? '
                                    '\n1. Verwijderen \n2. Terugkeren naar het hoofdmenu'))
        if delete_password ==1:
            opgeslagen_wachtwoorden.clear()
            print('Alle wachtwoord entries verwijdert.')
            return
        elif delete_password==2:
            return
        else:
            print(f'"{delete_password}" is een ongeldige keuze!')

while True:
    wachtwoord_menu = menu()
    clear_screen()
    if wachtwoord_menu==1:
        new_entry()
        print(lijn)
    elif wachtwoord_menu==2:
        list_passwords()
        print(lijn)
    elif wachtwoord_menu==3:
        search_password()
        print(lijn)
    elif wachtwoord_menu==4:
        pop_password()
        print(lijn)
    elif wachtwoord_menu==5:
        reset_list()
        print(lijn)
    elif wachtwoord_menu==6:
        print("Bedankt voor het gebruiken van de wachtwoordgenerator. \nDe applicatie wordt nu afgesloten.")
        break
    else:
        print(f'"{wachtwoord_menu}" is een ongeldige keuze!')
