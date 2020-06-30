""""
 Dans cet exercice, vous allez créer un
programme qui lit une année puis le nom d'un mois respectivement saisis par
l'utilisateur. Ensuite, votre programme devrait afficher le nombre de jours de ce mois.

Si le nom du mois saisi est fevrier et si l’année est bissextile alors le nombre de jours
de fevrier est 29. Si l’année n’est pas bissextile, alors le nombre de jours de fevrier
est 28. Pour faire plus simple, le nom du mois saisi par l’utilisateur doit être converti
en minuscule par le programme et ne doit pas comporté d’accent.
"""


annee_saisie = int(input("Veuiller saisir une annee "))

mois = input("Veuiller saisir un mois ex:[mai] ")

mois_saisie = mois.lower()

#cette variable me permet de changer le nombre de jours du mois de fevrier si l'annee n'est pas bissextile
fevrier = 28

char = {'janvier':'31', 'fevrier':'29', 'mars':'31', 'avril':'30', 'mai':'31', 'juin':'30', 'juillet':'31', 'aout':'31', 'septembre':'30', 'octobre':'31', 'novembre':'30', 'decembre':'31' }




#gerer le mois de fevrier

#si l'annee saisie est bissextile exexcute ce code
if (annee_saisie % 400 == 0) or ((annee_saisie % 4 ==0) & (annee_saisie / 100 !=0)):
    for i in char:
        if mois_saisie == i:
            print(mois_saisie, " contient ", "{}".format(char[i]), "jours")
        else:
            print("mois invalide")
            break

#si l'annee saisie n'est pas bissextile exexcute ce code
else:
    #je change le nombre de jour de fevrier par 28
    char['fevrier'] = fevrier
    for i in char:
        if mois_saisie == i:
            print(mois_saisie, " contient ", "{}".format(fevrier), "jours")
        else:
            print("mois invalide")
            break















