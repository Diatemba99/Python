""""
Dans cet exercice, vous allez créer un programme qui lit une lettre de l'alphabet
saisie par l'utilisateur. Si l'utilisateur entre a, e, i, o ou u, votre programme devrait
afficher un message indiquant que la lettre saisie est une voyelle. Sinon, votre
programme devrait afficher un message indiquant que la lettre est une consonne.
"""
caractere = input("saisissez un caractere ")
voyelle = ["a", "e", "i", "o", "u", "y"]

if caractere in voyelle:
    print(caractere,"est une voyelle")
else:
    print(caractere,"est une consonne")
