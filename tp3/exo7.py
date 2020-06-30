""""
Créez un jeu où l'ordinateur choisit un mot au hasard et le joueur doit deviner ce mot.
L'ordinateur indique au joueur le nombre de lettres dans le mot. Ensuite, le joueur a
cinq chances de demander si une lettre est dans le mot. L'ordinateur ne peut
répondre que par «oui» ou «non». Ensuite, le joueur doit deviner le mot.
"""
#choisir un mot au hasard
import random
import os

dico_mots = ["python", "coding", "boucle", "tuples", "listes"]

mot_a_deviner= random.choice(dico_mots)

coup = 5

#j'affichais le mot a deviner four faire le test
#print("le mot: ",mot_a_deviner)
print("-"*13)
print('---INDICES---')
print("le mot a deviner est composé de : ", len(mot_a_deviner),"caracteres")

#boucle principale du jeu
for jeu in range(5):

    #deviner le mot
    mot_saisie = input("veuillez deviner le mot : ")
    mot =  mot_saisie.lower()

    #s'il trouve le mot
    for i in dico_mots:
        if mot == mot_a_deviner:
            print("bravo vous avez trouver le mot magique")
            break
        else:
            # si une des lettres saisie par user se trouve dans le mot le pc repond oui ou non
            for i in mot_a_deviner:
                for j in range(len(mot)):
                    if i in mot:
                        print("oui",i,"en fait parti")
                        break
                    elif i != mot:
                        print("non")
                        #os.system("color E")
                        break


            coup = coup - 1
            print("il vous reste",coup, "tentatives")
            break
    #quitter le jeu dès que le mot est trouvé
    if mot == mot_a_deviner:
        break
    # s'il epuise le nombre de tentatives
    if coup == 0:
        print("game over")







