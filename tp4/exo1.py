"""
Déterminer la sortie du programme suivant
societes = [("Sonatel", "Mermoz", "Dakar"), ("CSS", "Richars Tall", Saint Louis"),
("Saprolait", "Faidherb", "Dakar")]
(nom, ville, region) = (societes [1][0], societes [1][1], societes [1][2])
print(nom, " est située à ", ville, ", ", region, '.',sep = " ")
"""

societes = [("Sonatel", "Mermoz", "Dakar"),
            ("CSS", "Richars Tall", "Saint Louis"),
            ("EDK", "Escale", "Kolda")
           ]
(nom, ville, region) = (societes [1][0], societes [1][1], societes [1][2])

print(nom, " est située à ", ville, ", ", region, '.',sep = " ")
