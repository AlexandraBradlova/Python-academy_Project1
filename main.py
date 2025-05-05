"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alexandra Brádlová  
email: alexandra.bradlova@gmail.com
"""

# Upravený text s některými slovy v UPPERCASE
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    AND nd steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top OF the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such AS paddlefish,
    garpike AND stingray are also present.
    '''
]

# Registrovaní uživatelé
registered_users = [
    {"user": "bob", "password": "123"},
    {"user": "ann", "password": "pass123"},
    {"user": "mike", "password": "password123"},
    {"user": "liz", "password": "Pass123"},
]

# Přihlášení uživatele
username = input("Enter your username: ").lower()

for user in registered_users:
    if user["user"] == username:
        password = input("Enter your password: ")
        if user["password"] == password:
            print(f"Welcome, {username.title()}!")
            break
        else:
            print("Incorrect password. Exiting...")
            quit()
else:
    print("Username not registered, program will end..")
    quit()

# Výběr textu
text_choice = input("Choose a text number - 1, 2 or 3: ")
if not text_choice.isdigit():
    print("Sorry. You must enter a number.")
    quit()

text_index = int(text_choice) - 1

if 0 <= text_index < len(TEXTS):
    chosen_text = TEXTS[text_index]
    print("You asked for text:\n" + chosen_text + "\n")
else:
    print("Incorrect choice of text. Shutting down.")
    quit()

# Analýza textu
special_characters = ".,!?;:-()\"'"

clean_words = [word.strip(special_characters) for word in chosen_text.split()]

words_total = len(clean_words)
title_words = [word for word in clean_words if word.istitle()]
uppercase = [word for word in clean_words if word.isupper()]
lowercase = [word for word in clean_words if word.islower()]
numbers = [int(word) for word in clean_words if word.isdigit()]
sum_numbers = sum(numbers)

# Výpis analýzy
oddelovac = "-" * 40
print(oddelovac)
print(f"Total words: {words_total}")
print(f"Titlecase words: {len(title_words)}")
print(f"Words in uppercase: {len(uppercase)}")
print(f"Words in lowercase: {len(lowercase)}")
print(f"Amount of numbers: {len(numbers)}")
print(f"Sum of numbers: {sum_numbers}")
print(oddelovac)

# Graf četnosti délek slov
frequency = {}
for word in clean_words:
    length = len(word)
    if length in frequency:
        frequency[length] += 1
    else:
        frequency[length] = 1

print("LEN  -   OCCURRENCES   -  COUNT")
print(oddelovac)
for length in sorted(frequency):
    count = frequency[length] #ze sloupec count je stejne delky jako promenna frequency
    print(f"{length:>3} | {'*' * count:<20} | {count}") #formatovani zapisu s jvezdickami stejne jako je len-occur-count radek
print(oddelovac)
