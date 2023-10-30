import random
import pickle

# Définition de l'intervalle du jeu
min_number = 0
max_number = 100

# Chargement de la base de données des scores depuis un fichier pickle
try:
    with open("score.pkl", "rb") as f:
        scores = pickle.load(f)
except FileNotFoundError:
    scores = {}

def get_user_name():
    while True:
        user_name = input("Entrez votre pseudo (sans espaces, en minuscules) : ")
        if ' ' not in user_name and user_name.islower():
            return user_name
        else:
            print("Le pseudo ne doit pas contenir d'espaces et doit être en minuscules.")

def play_game(user_name):
    # Génération d'un nombre secret
    secret_number = random.randint(min_number, max_number)
    remaining_attempts = 4 # Définir le nombre d'essais en fonction de l'intervalle

    while remaining_attempts > 0:
        try:
            user_guess = int(input(f"Devinez le nombre ({min_number}-{max_number}) : "))
            if min_number <= user_guess <= max_number:
                if user_guess == secret_number:
                    print("BRAVO ! Vous avez deviné le nombre.")
                    score = remaining_attempts * 30
                    print(f"Votre score dans cette partie : {score}")
                    if user_name in scores:
                        scores[user_name] += score
                    else:
                        scores[user_name] = score
                    with open("scores.pkl", "wb") as f:
                        pickle.dump(scores, f)
                    break
                elif user_guess < secret_number:
                    print("Le nombre secret est plus grand.")
                else:
                    print("Le nombre secret est plus petit.")
                remaining_attempts -= 1
                print(f"Il vous reste {remaining_attempts} essai(s).")
            else:
                print(f"Le nombre doit être entre {min_number} et {max_number}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    else:
        print(f"Perdu ! Le nombre secret était {secret_number}.")

if __name__ == "__main__":
    print("Bienvenue dans le jeu de roulette.")
    while True:
        user_name = get_user_name()
        play_game(user_name)
        play_again = input("Voulez-vous jouer à nouveau ? (Pour arrêter, appuyez sur la touche 'K'. Pour continuer à jouer, appuyez sur n'importe quelle autre lettre.) : ")
        if play_again.upper() == 'K':
            break
