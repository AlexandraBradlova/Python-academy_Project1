"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alexandra Brádlová  
email: alexandra.bradlova@gmail.com
"""

#ZMENILA JSEM NEKTERA SLOVA NA UPPERCASE OPROTI PUVODNIMU TEXTU
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

#CAST KDE USERNAME A PASSWORD SOUHLASI S REGISTROVANYMI UZIVATELI / NEBO NE
registered_users = [
    {"user":"bob", "password":"123"},
    {"user":"ann", "password":"pass123" },
    {"user":"mike", "password":"password123"},
    {"user":"liz", "password":"Pass123"},
    ]

username = input("Enter you username:").lower()

for user in registered_users:
    if user["user"] == username:
        password = input("Enter your password: ")
        if user["password"] == password:
            print(f"Welcome, {username.title()}!")
        else:
            print("Incorrect password. Exiting...")
        break
else:
    print("Username not registered, program will end..")


#CAST 2 - vybrat si z dostupnych textů nebo akcí:
'''Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.'''

text_choice = input("Choose a text number - 1, 2 or 3:")
#nelze jen za pouziti INT!!! protoze vystup input je vzdy string
if not text_choice.isdigit():
    print("Sorry.You must enter a number.")
    quit()

text_index = int(text_choice) - 1  #ted teprve prevedu input na int a dodam aby bylo jasne ze cislo textu == index textu v TEXTS o 1 nižší

if 0 <= text_index < len(TEXTS):
    #len je tady proto aby se nedalo zadat vyssi cislo nez je mozstvi cisel textu
    chosen_text = TEXTS[text_index]
    print("You asked for text:\n" + chosen_text + "\n")
else:
    print("Incorrect choice of text. Shutting down.")

#CAST 3 - analyzovat zvoleny text
'''
 počet slov,
 počet slov začínajících velkým písmenem
 počet slov psaných velkými písmeny,
 počet slov psaných malými písmeny,
 počet čísel (ne cifer),
 sumu všech čísel (ne cifer) v textu.
'''

special_characters = ".,!?;:-()\"'"

clean_words = []

for word in chosen_text.split():
    word = word.strip(special_characters)
    clean_words.append(word)

words_total = len(clean_words)
#title_words = [clean for clean in clean_words if clean.istitle()]
uppercase = [word for word in clean_words if word.isupper()]
lowercase = [word for word in clean_words if word.islower()]
numbers_as_text = [word for word in clean_words if word.isdigit()]
numbers = 0
for word in clean_words:
    if word.isdigit():
        numbers += 1
sum_numbers = sum(int(word) for word in numbers_as_text)

# vypsat vypocty

print("-" * 40) #oddelovac
print(f"Total words: {words_total}")
#print(f"Titlecase words: {len(title_words)}")
print(f"Words in uppercase: {len(uppercase)}")
print(f"Words in lowercase: {len(lowercase)}")
print(f"Amount of numbers written as text: {len(numbers_as_text)}")
print(f"Amount of numbers: {numbers}")
print(f"Sum of numbers: {sum_numbers}")
print("-" * 40) #oddelovac