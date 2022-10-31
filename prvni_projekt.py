'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Janků
email: michal.janku@cdv.cz
discord: Michal J.#5035
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "-"*40

# Uložené přihlašovací údaje
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

# Požádání uživatele o zadání hodnot pro proměnné "username" a "password"
username = input('Username: ')
password = input('Password: ')
print(oddelovac)

# Ověření jestli zadané jméno a heslo souhlasí s uloženými údaji ve složce "users"
if users.get(username) == password:

    # ... pokud souhlasí, přivítám uživatele jménem
    print('Welcome to the app,', username, "!")
    print('We have 3 texts to by analyzed.')
    print(oddelovac)
    # ... pokud nesouhlasí, upozorním jej na chybné údaje
else:
    print('Unregistered user or wrong password, terminating the program...')
    quit()

# Nechám uživatele vybrat text
number_text = input('Enter a number btw. 1 and 3 to select: ')

# Ověření jestli je číslo textu v pořádku
if number_text.isnumeric() and 1 <= int(number_text) <= 3:
    print(oddelovac)
else:
    print('The entered value is not correct, terminating the program...')
    quit()

# odstraním mezery na začátku a na konci textu, převedu "\n" a "-" na mezery, rozdělím `str` na `list`
jednotliva_slova = TEXTS[int(number_text) - 1].strip().replace("\n", " ").replace("-", " ").split(" ")

# vyčistím text od diakritiky
vycistena_slova = list()
for slovo in jednotliva_slova:
    vycistena_slova.append(slovo.strip(",.:;?!"))

# určím počet slov v textu
pocet_slov = len(vycistena_slova)
print(f'There are {pocet_slov} words in selected text.')

# počet slov začínajících velkým písmenem
velke_pismeno = int()
for slovo in vycistena_slova:
    if slovo.istitle():
        velke_pismeno += 1
print(f'There are {velke_pismeno} titlecase words.')

# počet slov psaných velkými písmeny
vsechna_velka = int()
for slovo in vycistena_slova:
    if slovo.isupper() and slovo.isalpha():
        vsechna_velka += 1
print(f'There are {vsechna_velka} uppercase words.')

# počet slov pouze s malými písmeny
vsechna_mala = int()
for slovo in vycistena_slova:
    if slovo.islower() and slovo.isalpha():
        vsechna_mala += 1
print(f'There are {vsechna_mala} lowercase words.')

# počet čísel
cisla = []
for slovo in vycistena_slova:
    if slovo.isnumeric():
        cisla.append(slovo)
print(f'There are {len(cisla)} numeric strings.')

# suma všech čísel
suma = int()
for cislo in cisla:
    suma += int(cislo)
print(f'The sum of all the numbers is {suma}.')

print(oddelovac)

# vytvoření listu s délkami slov
delky_slov = []
for slovo in vycistena_slova:
    delky_slov.append(len(slovo))

# četnost různých délek slov
vyskyt_delek = dict()

for delka in delky_slov:
    # pokud nemám, přidám délku (klíč) do slovníku
    if delka not in vyskyt_delek:
        vyskyt_delek[delka] = 1  # první výskyt
    # pokud mam, zvysim hodnotu o jedna
    else:
        vyskyt_delek[delka] = vyskyt_delek[delka] + 1  # dalsi vyskyt

# výpis četností různě dlouhých slov
print('LEN|    OCCURENCES    |NR.')
print(oddelovac)
for delka, vyskyt in sorted(vyskyt_delek.items()):
    vyskyt_graf = vyskyt * '*'
    print(f'{delka:>3}|{vyskyt_graf:<18}|{vyskyt:<3}', sep='\n')
