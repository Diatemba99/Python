""""
Ecrivez un programme qui affiche toutes les lettres d’une chaîne présentent dans
une chaîne2
"""
chaine = input("taper le premier mot ")
chaine2 = input("taper le deuxieme mot ")

#je parcours chaque caractere du premier mot
for i in chaine:
    # je parcours chaque caractere du deuxieme mot
    for j in chaine2:
        #j'affiche les caracteres present dans les deux mots
        if i == j:
            print(i)
