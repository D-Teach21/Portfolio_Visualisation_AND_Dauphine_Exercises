first = "Lucky"
last = "Ramdoyal"
full = f"{first} {last}"
print(full)
##%
course = "Python Programming"
print(course.title())
print(course.upper())
print(course.lower())

##%
x = 1
x = 1.1
x = 1 + 2j

#%%
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 1)
print(10 ** 3)
#%%
x = 10
x = x + 3
x += 3

##%
import math
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

##%

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

#int(x)
#float(x)
#bool(x)
#str(x)

#%%

année = input("Saisir l'année d'aujourd'hui: ")
demain = int(année) + 1
print(f"Demain nous serons en {demain}")

#%%

temperature = input("Quelle est la temérature aujourd'hui? ")
if 30< int(temperature) < 50:
    print("It's warm")
    print("Drink water")
elif int(temperature) > 50:
    print("Oh ma fucking days go to Russia or Sweden")
else :
    print("Go get a radiator")

##%

high_income = True
good_credit = True
student = False

if high_income or good_credit and not student:
    print("eligible")

#%%
if 10 =="10":
    print("a")
elif"bag" > "apple" and "bag"> "cat":
    print("b")
else:
    print("c")

#%%
for number in range(0, 13, 3):
    print("attempt", number, number * ".")

# %%
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
# %%
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
# %%
number = 100
while number > 0:
    print(number)
    number /= 2
# %%
count = 0
for number in range (1, 10):
    if number %2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

# %%
round(2.6)
# %%
def naruto(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


naruto(first_name = input("Saisir votre prénom: "), last_name = input("Saisir votre nom de famille: "))

# %%
def increment(number, by=1):
    return number + by


print(increment(2, 5))
# %%
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(2, 4, 5, 5)
# %%
#Exercice numéro 2 du 1er doc Dauphine
first_name = input("Hey toi là, donnes moi ton prénom: ")
last_name = input("Ah je veux aussi que tu me donnes ton nom de famille: ")
city = input("C'est quoi ta ville ? ")
age = int(input("Ah et juste pour savoir si tu es éligible donne nous ton âge: "))
print(f"Je m'appelle {first_name} {last_name}; j'ahbite à {city} et j'ai {age} ans")
sub_duration = int(input("Dernière question, combien de temps pensez-vous rester chez nous ? "))
futur_age = (age + sub_duration)
print(f"Ainsi j'aurai {futur_age} ans dans {sub_duration} ans")

#%%
x = int(input("Saisir un nombre: "))
y = int(input("saisir un nombre: "))
print(f"y est égale à {x} et x est égale à {y}")

# %%
print(" _____     _____     _____")
print("| . . | * | . . | * | . . |")
print(str(" \_o_/  *  \_x_/  *  \_v_/"))
# %%
count = 200
for number in range (1, 10):
    if number %2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
# %%
x = int(input("Quelle est la valeur de x? "))
print(f"x = {x}, 2x = {2*x}, 3x = {3*x}, 4x = {4*x}, 8x = {8*x}", sep="\n")
# %%
#Exercice 2 du semestre 2
Taille = float(input("Peux-tu me donner ta taille en m? "))
Masse = float(input("Chef peux-tu me donner ton poids par pitié en kg! "))
IMC = Masse/(Taille*Taille)
print(f"Roulement de tambour... ton IMC est de {IMC}")
if 18.5 <= IMC <= 25:
    print("Mais CHEF TON IMC montre que t'es dans le bueno")
else:
    print("Houla euh va falloir que tu fasses quelque chose là hein")
#%%
x = float(input("Donne moi un nombre auquel tu penses là maintenant "))
y = float(input("Donne un autre stp "))
z = float(input("Bon dernier des derniers "))
if x == y + z or y == x + z or z == x + y:
    print("Bah c'est carré ça mon chef")
else:
    print("Ah bah celui-ci c'est pas bon")
#%%
n = float(input("Alors on va voir si t'es bon à l'école donne moi ta moyenne général: "))
if n < 10:
    print("Aie aie aie tu es ajourné")
elif 10 <= n < 12:
    print("Hmmm mouais c bof bof hein mais bon je te donnes Passable")
elif 12 <= n < 14:
    print("Bon le niveau est correct chef c'est AB")
elif 14 <= n < 16:
    print("Sheeeesh c bon ça t'es cho mon chef t'es B")
elif n >= 16:
    print("Mais c'est que t'es une brute chef c'est TB")
#ou sinon je peux mettre en dernière ligne else: saut d'1 ligne print("TB")
#%%
année = int(input("Saisir une anneé quelquonque: "))
if (année % 4 == 0) and not (année % 100 == 0) or (année % 400 == 0):
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile ou est ordinaire")
#%%
v = int(input("Donner n'importe quelle valeur et voir s'il est dans l'intervalle auquel je pense: "))
if 0<= v <= 9:
    print("La valeur {v}, est bien comprise dans l'intervalle [0 ; 9]")
else:
    print("Malheuresement ça n'est pas dans mon intervalle")
#%%
#Dérivé de l'exo précédent
v = float(input("Donner une valeur qui sort de votre imaginaire: "))
if v < 0 or v > 9:
    print("Parfait tu n'es pas dans mon intervalle tu survies")
else:
    print("Mince tu es dans mon intervalle qui est [0 ; 9]")
#%%
first_name = input("Saisir votre prénom: ")
last_name = input("Saisir votre nom de famille: ")
city = input("Saisir votre ville de naissance: ")
birth_department = int(input("Sasir votre département de naissance: "))
print(f"Vous vous appelez {first_name} {last_name}." , f"Vous êtes né(e) à {city} ({birth_department})", sep = "\n")
if 1 <= birth_department <= 95 or 971 <= birth_department <= 974 or birth_department == 976:
    print("Votre numérode département est validé ✅")
else:
    print("Votre numéro de département est éronné ❌!")
#%%
année = int(input("Saisir l'année courante: "))
month = int(input("Saisir le numéro du mois courant: "))
if 0 < month <= 12:
    print("Nous chargeons la suite de la réponse")
    if 0 < month <= 7 and (month % 2 == 0) and (month != 2):
        print(f"{month} compte 30 jours")
    elif 0 < month <= 7 and (month % 2 == 1) and (month != 2):
        print(f"Le mois {month} compte 31 jours")
        if (month == 2) and (année % 4 == 0) and not (année % 100 == 0) or (année % 400 == 0):
            print("Encore une exception lors d'une année bissextile février compte 29 jours!")
        elif (month == 2) and (année % 4 == 1) or (année % 100 == 0) or (année % 400 == 1):
            print("Le mois de février va là compter 28 jours")
    if 8 <= month <= 12 and (month % 2 == 0):
        print(f"Le mois {month} compte 31 jours")
    elif 8 <= month <= 12 and (month % 2 == 1):
        print(f"Le mois {month} compte 30 jours")
else:
    print("Vous devez saisir un numéro compris dans [1 ; 12]!")
#%%
longueur_a = float(input("Saisir la longueur a du triangle: "))
longueur_b = float(input("Saisir la longueur b du triangle: "))
longueur_c = float(input("Saisir la longueur c du triangle: "))
if (longueur_a + longueur_b < longueur_c) or (longueur_c + longueur_b < longueur_a) or (longueur_c + longueur_a < longueur_b):
    print(f"Il est possible de construire un triangle de côtés {longueur_a}, {longueur_b} et {longueur_c}")
if (longueur_a**2 == longueur_b**2 + longueur_c**2) or (longueur_b**2 == longueur_a**2 + longueur_c**2) or (longueur_c**2 == longueur_a**2 + longueur_b**2):
    print("Le triangle est rectangle")
elif (longueur_a == longueur_b and longueur_b == longueur_c):
    print("le triangle est dit équilatéral")
else:
    print("Le triangle est quelconque")
# %%
x = 0
result = 0
while x < 100:
    if x % 2 != 0:
        result = result + x
    x = x + 1  # Maintenant, x augmente à chaque tour !

print("La somme des entiers impairs inférieurs à 100 est :", result)
# %%
# exercice 3.2
x = 6000
time = 0
while x <= 7000:
    x = x + (x * 0.15)
    time = time + 1
print("Au bout de", time, "ans, ", end="")
print("vous aurez plus de 7000 euros sur votre livret.")
#%%
#pour calculer des puissances
x = float(input("Saisir une valeur pour x: "))
while x < 0: #au cas où l'utilisateur écrit x négatif
    x = float(input("Saisir une valeur positive de -x: "))
n = int(input("Saisir une valeur pour n: "))
while n < 0:
    n = int(input("Saisir une valeur positive de -n: "))
i = 0
r = 1
while i < n:
    r = r * x
    i = i + 1
print("x^n =", r)
#%%
x = int(input("Saisir une valeur strictement positive: "))
while x <= 0:
    x = int(input("Saisir une valeur strictement positive de x: " ))
i = 1
r = 0
while i <= x:
    if x % i == 0:
        r = r + i
    i = i + 1
print(f"La somme des diviseurs de {x}, est égale à {r}")
#%%
# 1. Saisie et validation (Cette partie était correcte)
x = int(input("Saisir une valeur strictement positive: "))
while x <= 0:
    x = int(input("Saisir une valeur strictement positive de x: " ))

# 2. Initialisation
i = 1
r = 0 # r contiendra la somme

# 3. Boucle de recherche des diviseurs
while i <= x: # On va jusqu'à x inclus (si vous voulez exclure x, remettez x // 2)
    if x % i == 0:     # Si le reste de la division est 0, c'est un diviseur
        r = r + i      # CORRECTION : On ajoute le diviseur 'i' à la somme, pas '1'
    i = i + 1          # CORRECTION : On passe au nombre suivant

# 4. Affichage du résultat
print(f"La somme des diviseurs de {x} est : {r}")
#%%
#somme des pairs et impairs
n = int(input("Saisir un entier positifif n: "))
while n <= 0:
    n = int(input("Erreur ❌ Veuillez saisir un entier positif n: "))
n_entiers = input("saisir des entiers positifs n: ")
nombres = list(map(int, n_entiers.split()))
while sum(nombres % 2 == 0) == sum(nombres % 2 != 0):
    tru = sum(nombres % 2 == 0)
    fals = sum(nombres % 2 != 0)
    if tru != fals:
        print(f"La somme des paris {tru}, est différente de celle des impairs {fals}")
print(f"La somme des nombres pairs est de {tru}, idem pour celle des imparis")
#ce n'est pas bon
#%%
# la correction complète
import numpy as np

# --- ÉTAPE 1 : Saisir et valider n ---
n = int(input("Combien de nombres allez-vous saisir ? (n) : "))

while n <= 0:
    n = int(input("Erreur ❌. Veuillez saisir un entier strictement positif pour n : "))

# --- ÉTAPE 2 : Saisir la liste et vérifier sa taille ---
while True:
    print(f"Veuillez maintenant saisir exactement {n} entiers (séparés par un espace) :")
    saisie = input("> ")
    
    # On coupe la chaîne pour compter les éléments
    elements = saisie.split()
    
    # LA VÉRIFICATION EST ICI :
    if len(elements) == n:
        # Si la taille est bonne, on convertit en NumPy et on sort de la boucle
        nombres = np.array(elements, dtype=int)
        break 
    else:
        # Sinon, on affiche une erreur et la boucle recommence
        diff = len(elements)
        print(f"⚠️ Erreur : Vous avez entré {diff} nombres alors que n = {n}.")
        print("Recommencez.\n")

# --- ÉTAPE 3 : Calculs avec NumPy (Vectorisation) ---
# Création des masques (comme vu précédemment)
masque_pair = (nombres % 2 == 0)
masque_impair = (nombres % 2 != 0)

# Calcul des sommes
somme_pairs = np.sum(nombres[masque_pair])
somme_impairs = np.sum(nombres[masque_impair])

# --- ÉTAPE 4 : Affichage ---
print("-" * 30)
if somme_pairs != somme_impairs:
    print(f"Les sommes sont différentes.")
    print(f"Somme PAIRS : {somme_pairs}")
    print(f"Somme IMPAIRS : {somme_impairs}")
else:
    print(f"Égalité parfaite ! La somme est de {somme_pairs}.")
#%%
#code pour n!
n = int(input("Saisir un entier naturel n: "))
while n < 0:
    n = int(input("Erreur: Veuillez saisir une valeur strictement positive: "))
factorielle = 1
tours = 1
while tours <= n:
    factorielle = factorielle * tours
    tours = tours + 1
print(f"Ainsi {n}! est égale à {factorielle}.")
#%%
n = int(input("Saisir un entier n: "))
while n < 0:
    n = int(input("Erreur: Par pitié veuillez saisir un entier n positif! : "))
n_entiers = input(f"Saisir {n} valeurs: ")
(list())
# %%
#je le retentes
import numpy as np
n = int(input("Il vous faut saisir un entier n: "))
while n <= 0:
    print("ERREUR")
    n = int(input("S'il-vous-plaît veuillez saisir un entier n strictement positif: "))
while True:
    print(f"Parfait maintenant nous vous demanderons de bien vouloir saisir ci-après une liste de {n} entiers (séparé par des ,)")
    saisie = input("> ")
    elements = saisie.split(",")
    if len(elements) == n:
        nombres = np.array(elements, dtype = int)
        break
    else:
        diff = len(elements)
        print(f"Erreur ❌: Vous avez saisie {diff} n valeur au lieu d'en écrire {n}")
        print("Il faut ainsi tout reprendre! /n")
pairs = nombres % 2 == 0
impairs = nombres % 2 != 0
S_pairs = np.sum(nombres[pairs])
S_impairs = np.sum(nombres[impairs])

if S_pairs != S_impairs:
    print(f"Oh nan, malheuresement votre liste contient une somme de valeurs pairs ({S_pairs}) différente de celle des impairs ({S_impairs})")
    print("Vous pouvez retenter votre chance! /n")
else:
    print(f"Félicitation ! Vous êtes parvenue à obtenir une liste de valeurs contenant une somme de valeur pairs égale à celle des impairs, plus précisément de {S_pairs}")
#%%
n = 4
tours = 1
résultat = []
while tours <= 3:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    résultat.append(n)
    tours = tours + 1
print(f"Voici la liste que l'on obtient pour n = 4, {résultat}")