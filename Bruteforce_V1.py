import random


# import pyautogui

mdp_a_touver = ""                                           # La variable est defini
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&é(-è_çà)=^$*ù!:;,<>°+£¨%µ§/.?~#'{[|`\^@]}¤" # La variable est defini

chars_list = list(chars)                                    # Defini la variable chars en liste

mdp = input("Entrez votre mot de passe : ")                 # L'utilisateur doit rentrer

while (mdp_a_touver != mdp):                                # Debut de la boucle
    mdp_a_touver = random.choices(chars_list, k=len(mdp))   # Generre une liste de caractere par rapport a la taille du mot de passe choisi

    print(str(mdp_a_touver))                                # Affiche et convertit les données en chaine

    if (mdp_a_touver == list(mdp)):
        print("Le mot de passe est : ", mdp_a_touver)       # Affiche le résultat trouvé
        break                                               # Quitte la boucle
