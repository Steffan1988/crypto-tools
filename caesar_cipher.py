letter_dict = {
    'a': 1,    'b': 2,    'c': 3,    'd': 4,    'e': 5,    'f': 6,    'g': 7,    'h': 8,    'i': 9,    'j': 10,
    'k': 11,    'l': 12,    'm': 13,    'n': 14,    'o': 15,    'p': 16,    'q': 17,    'r': 18,    's': 19,    't': 20,
    'u': 21,    'v': 22,    'w': 23,    'x': 24,    'y': 25,    'z': 26
}
reverse_dict = {
    1: 'a',    2: 'b',    3: 'c',    4: 'd',    5: 'e',    6: 'f',    7: 'g',    8: 'h',    9: 'i',    10: 'j',
    11: 'k',    12: 'l',    13: 'm',    14: 'n',    15: 'o',    16: 'p',    17: 'q',    18: 'r',    19: 's',    20: 't',
    21: 'u',    22: 'v',    23: 'w',    24: 'x',    25: 'y',    26: 'z'
}

def encryptie():
    """"deze functie encrypt je input"""
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    # Neem eerst het getal van de letter uit het woordenboek "letter_dict"
    encrypted = []
    for i in message:
        x = i
        encrypted.append(letter_dict[x])
    # Tel daarna bij ieder getal uit de lijst "encrypted" de waarde van shift op
    encrypted_shift = [getal + shift for getal in encrypted]
    # Voor ieder getal uit "encrypted_shift" zoek de value uit het woordenboek "reverse_dict"
    # en stop deze in de lijst "encrypted_word"
    encrypted_word = []
    for i in encrypted_shift:
        y = i
        if y >26:
            y -=26
        encrypted_word.append(reverse_dict[y])
    encrypted_joined = ("".join(encrypted_word))
    print(f'The encoded text is: {encrypted_joined}')
    return

def decryptie():
    """"deze functie decrypt je input"""
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    # Neem eerst het getal van de letter uit het woordenboek "letter_dict"
    decrypted = []
    for i in message:
        x = i
        decrypted.append(letter_dict[x])
    # Trek daarna bij ieder getal uit de lijst "decrypted" de waarde van shift af
    decrypted_shift = [getal - shift for getal in decrypted]
    # Voor ieder getal uit "decrypted_shift" zoek de value uit het woordenboek "reverse_dict"
    # en stop deze in de lijst "encrypted_word"
    decrypted_word = []
    for i in decrypted_shift:
        y = i
        if y >26:
            y -=26
        elif y <=0:
            y +=26
        decrypted_word.append(reverse_dict[y])
    decrypted_joined = ("".join(decrypted_word))
    print(f'The decoded text is: {decrypted_joined}')
    return

def menu():
    """vraagt de gebruiker een keuze te maken."""
    menu_choice = int(input(
        "Welcome to the Caesar Cipher!\n"
        "What would you like to do?\n"
        "1. Encrypt a word\n"
        "2. Decrypt a word\n"
        "3. Exit the app\n"
        "Make a choice (1-3): "
    ))
    return menu_choice

def repeat():
    """Vraagt de gebruiker of ze nog een handeling willen doen."""
    while True:
        one_more = int(input("Once more? \n1:Yes \n2:No"))
        if one_more == 1:
            return True
        elif one_more == 2:
            return False
        else:
            print(f"{one_more} is an invalid option! Please choose 1 or 2.")

while True:
    choice = menu()
    if choice == 1:
        encryptie()
    elif choice == 2:
        decryptie()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print(f"{choice} is an invalid choice.")
        continue

    if not repeat():
        print("Thanks for using this application")
        break
